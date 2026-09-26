#!/usr/bin/env python3

import sys
import tempfile
import subprocess
import wave
from pathlib import Path

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run

RATE = 16000
BLOCK = 1280
DEVICE = None
SILENCE_THRESHOLD = 180
SILENCE_SECONDS = 1.3
MAX_SECONDS = 15

PIPER_MODEL = BASE / "voice_models/en_US-hfc_female-medium.onnx"

_whisper = None


def whisper_model():
    global _whisper

    if _whisper is None:
        _whisper = WhisperModel(
            "base.en",
            device="cpu",
            compute_type="int8"
        )

    return _whisper


def speak(text):
    text = str(text).strip()

    if not text:
        return

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as tmp:
        path = Path(tmp.name)

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "piper",
                "-m",
                str(PIPER_MODEL),
                "-f",
                str(path)
            ],
            input=text,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        subprocess.run(
            ["aplay", str(path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )

    finally:
        path.unlink(missing_ok=True)


def record_command():
    frames = []
    started = False
    silent = 0

    stop_after = int(
        SILENCE_SECONDS * RATE / BLOCK
    )

    maximum = int(
        MAX_SECONDS * RATE / BLOCK
    )

    with sd.InputStream(
        samplerate=RATE,
        channels=1,
        dtype="int16",
        blocksize=BLOCK,
        device=DEVICE
    ) as stream:

        for _ in range(maximum):
            audio, _ = stream.read(BLOCK)

            audio = np.squeeze(audio).astype(
                np.int16
            )

            level = float(
                np.mean(
                    np.abs(
                        audio.astype(np.float32)
                    )
                )
            )

            if level >= SILENCE_THRESHOLD:
                started = True
                silent = 0
                frames.append(audio.copy())

            elif started:
                frames.append(audio.copy())
                silent += 1

                if silent >= stop_after:
                    break

    if not frames:
        return None

    return np.concatenate(frames)


def transcribe(audio):
    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as tmp:
        path = Path(tmp.name)

    try:
        with wave.open(str(path), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(RATE)
            f.writeframes(audio.tobytes())

        segments, _ = whisper_model().transcribe(
            str(path),
            language="en",
            beam_size=5
        )

        return " ".join(
            segment.text.strip()
            for segment in segments
        ).strip()

    finally:
        path.unlink(missing_ok=True)


def run_once():
    # Button was pressed, so no wake word is required.
    speak("Yes?")

    audio = record_command()

    if audio is None:
        return {
            "status": "FAIL",
            "command": "",
            "response": "I didn't hear anything."
        }

    command = transcribe(audio)

    if not command:
        return {
            "status": "FAIL",
            "command": "",
            "response": "I didn't understand that."
        }

    result = run(command)

    if isinstance(result, dict):
        response = (
            result.get("model_response")
            or result.get("message")
            or result.get("stdout")
            or str(result)
        )
    else:
        response = str(result)

    speak(response)

    return {
        "status": "PASS",
        "command": command,
        "response": response
    }
