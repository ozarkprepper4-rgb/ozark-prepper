#!/usr/bin/env python3

import sys
import subprocess
import tempfile
import wave
from pathlib import Path

import numpy as np
import sounddevice as sd
import openwakeword
from openwakeword.model import Model
from faster_whisper import WhisperModel

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run

RATE = 16000
BLOCK = 1280
DEVICE = None  # Use Linux/PortAudio default input device

PIPER_MODEL = BASE / "voice_models/en_GB-alba-medium.onnx"

WAKE_MODEL = (
    Path(openwakeword.__file__).parent
    / "resources/models/hey_jarvis_v0.1.onnx"
)

WAKE_THRESHOLD = 0.50
SILENCE_THRESHOLD = 180
SILENCE_SECONDS = 1.3
MAX_RECORD_SECONDS = 12


def speak(text):
    text = str(text).strip()
    if not text:
        return

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = Path(tmp.name)

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "piper",
                "-m",
                str(PIPER_MODEL),
                "-f",
                str(wav_path),
            ],
            input=text,
            text=True,
            check=True,
        )

        subprocess.run(
            ["aplay", str(wav_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    finally:
        wav_path.unlink(missing_ok=True)


def record_command():
    frames = []
    speech_started = False
    silent_blocks = 0

    blocks_for_silence = int(
        SILENCE_SECONDS * RATE / BLOCK
    )

    max_blocks = int(
        MAX_RECORD_SECONDS * RATE / BLOCK
    )

    print("LISTENING FOR COMMAND...")

    with sd.InputStream(
        samplerate=RATE,
        channels=1,
        dtype="int16",
        blocksize=BLOCK,
        device=DEVICE,
    ) as stream:

        for _ in range(max_blocks):
            audio, _ = stream.read(BLOCK)
            mono = np.squeeze(audio).astype(np.int16)

            level = float(np.mean(np.abs(mono)))

            if level >= SILENCE_THRESHOLD:
                speech_started = True
                silent_blocks = 0
                frames.append(mono.copy())
            elif speech_started:
                frames.append(mono.copy())
                silent_blocks += 1

                if silent_blocks >= blocks_for_silence:
                    break

    if not frames:
        return None

    audio = np.concatenate(frames)

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False,
    ) as tmp:
        path = Path(tmp.name)

    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(RATE)
        f.writeframes(audio.tobytes())

    return path


def transcribe(model, audio_path):
    segments, _ = model.transcribe(
        str(audio_path),
        language="en",
        beam_size=5,
    )

    return " ".join(
        segment.text.strip()
        for segment in segments
    ).strip()


def wait_for_wake(wake_model):
    print()
    print('WAITING — say "Hey Jarvis"')
    print()

    with sd.InputStream(
        samplerate=RATE,
        channels=1,
        dtype="int16",
        blocksize=BLOCK,
        device=DEVICE,
    ) as stream:

        while True:
            audio, _ = stream.read(BLOCK)
            mono = np.squeeze(audio)

            prediction = wake_model.predict(mono)

            for name, score in prediction.items():
                score = float(score)

                if score >= WAKE_THRESHOLD:
                    print(
                        "WAKE DETECTED:",
                        name,
                        round(score, 3),
                    )

                    # Flush residual wake-word audio before recording command.
                    sd.sleep(500)
                    return


def voice_command_once(status_callback=None):
    """Run one complete wake -> listen -> transcribe -> Destiny -> speak cycle."""

    def status(value):
        if status_callback:
            status_callback(value)
        print(value)

    status("LOADING VOICE")

    whisper = WhisperModel(
        "base.en",
        device="cpu",
        compute_type="int8",
    )

    wake = Model(
        wakeword_model_paths=[str(WAKE_MODEL)]
    )

    status('WAITING FOR WAKE WORD')
    wait_for_wake(wake)

    status("LISTENING")
    speak("Yes?")

    # Give playback time to release the audio device and avoid capturing
    # Destiny's own acknowledgement.
    sd.sleep(350)

    audio_path = record_command()

    if audio_path is None:
        status("WAITING")
        return None

    status("TRANSCRIBING")

    try:
        command = transcribe(whisper, audio_path)
    finally:
        audio_path.unlink(missing_ok=True)

    if not command:
        speak("I didn't understand that.")
        status("WAITING")
        return None

    # Strip temporary wake phrase if Whisper captured any residue.
    lowered = command.lower()
    for prefix in (
        "hey jarvis,",
        "hey jarvis.",
        "hey, jarvis.",
        "hey, jarvis,",
        "hey jarvis",
        "hey, jarvis",
    ):
        if lowered.startswith(prefix):
            command = command[len(prefix):].strip()
            break

    status("PROCESSING")

    result = run(command)

    if isinstance(result, dict):
        response = (
            result.get("model_response")
            or result.get("message")
            or str(result)
        )
    else:
        response = str(result)

    status("SPEAKING")
    speak(response)
    status("WAITING")

    return {
        "command": command,
        "response": response,
        "result": result,
    }


def main():
    print("=== DESTINY VOICE OPERATOR ===")
    print("Loading speech recognition...")

    whisper = WhisperModel(
        "base.en",
        device="cpu",
        compute_type="int8",
    )

    print("Loading wake detector...")

    wake = Model(
        wakeword_model_paths=[str(WAKE_MODEL)]
    )

    print("VOICE SYSTEM ONLINE")
    print("Press Ctrl+C to stop.")

    while True:
        try:
            wait_for_wake(wake)

            speak("Yes?")

            audio_path = record_command()

            if audio_path is None:
                speak("I didn't hear a command.")
                continue

            try:
                command = transcribe(
                    whisper,
                    audio_path,
                )
            finally:
                audio_path.unlink(missing_ok=True)

            if not command:
                speak("I didn't understand that.")
                continue

            print()
            print("NEIL:", command)
            print("DESTINY: processing...")
            print()

            result = run(command)

            if isinstance(result, dict):
                response = (
                    result.get("model_response")
                    or result.get("message")
                    or str(result)
                )
            else:
                response = str(result)

            print("DESTINY:", response)
            print()

            speak(response)

        except KeyboardInterrupt:
            print()
            print("Destiny voice operator stopped.")
            break

        except Exception as e:
            print()
            print("VOICE ERROR:", e)
            print()

            try:
                speak("I encountered a voice system error.")
            except Exception:
                pass


if __name__ == "__main__":
    main()
