#!/usr/bin/env python3
import json, re, shutil, subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
def load_html():
    return (ROOT / "destiny_chat.html").read_bytes()
FACE = Path("/home/destiny/Obsidian/Destiny/destiny_avatar.jpg")
TASK = ROOT / "destiny_task.py"

def voice():
    for n in ("espeak-ng", "espeak"):
        if shutil.which(n):
            return n
    return None

LOCK_FILE = Path("/tmp/destiny_model_busy.lock")

def ask(text):
    LOCK_FILE.write_text("destiny_chat_server")
    try:
        t = (text or "").strip()
        wm = re.search(r"into\s+(/home/destiny/Obsidian/[^\s:]+)\s*:\s*(.+)", t, re.I|re.S)
        if re.search(r"\bwrite\b|\bcreate\b", t, re.I) and wm:
            path = Path(wm.group(1))
            line = re.sub(r"\s*Do not ask.*$", "", wm.group(2), flags=re.I|re.S).strip()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(line + "\n", encoding="utf-8")
            return f"Wrote {path.name}."
        p = subprocess.run(["python3", str(TASK), t], capture_output=True, text=True, timeout=300)
        raw = (p.stdout or "") + (("\n" + p.stderr) if p.stderr else "")
        m = re.search(r"Destiny:\s*(.*?)(?:=== PIPELINE ===|DESTINY_TASK_COMPLETE|$)", raw, re.S)
        return (m.group(1).strip() if m else raw.strip()) or "No reply."
    finally:
        LOCK_FILE.unlink(missing_ok=True)

def listen():
    wav = "/tmp/destiny_mic.wav"
    source = subprocess.run(
        ["pactl", "get-default-source"],
        capture_output=True, text=True, timeout=5
    ).stdout.strip()

    subprocess.run([
        "timeout", "8", "parec",
        f"--device={source}",
        "--rate=16000",
        "--channels=1",
        "--format=s16le",
        "--file-format=wav",
        wav
    ], timeout=10)

    code = (
        "from faster_whisper import WhisperModel; "
        "m=WhisperModel('base.en',device='cpu',compute_type='int8'); "
        f"s,_=m.transcribe('{wav}',beam_size=5); "
        "print(' '.join(x.text.strip() for x in s))"
    )

    r = subprocess.run(
        [str(ROOT / "voice_env/bin/python"), "-c", code],
        capture_output=True, text=True, timeout=60
    )
    return r.stdout.strip()

def speak(text):
    kokoro_model = "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/voice/kokoro-v1.0.onnx"
    kokoro_voices = "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/voice/voices-v1.0.bin"
    clean = re.sub(r"\s+", " ", re.sub(r"[=*`#]+", " ", str(text or ""))).strip()[:400]
    if not clean:
        return
    wav = "/tmp/destiny_speak.wav"
    text_file = "/tmp/destiny_speak_text.txt"
    Path(text_file).write_text(clean, encoding="utf-8")
    subprocess.run(["kokoro-tts", text_file, wav, "--voice", "bf_emma", "--model", kokoro_model, "--voices", kokoro_voices], timeout=30)
    subprocess.Popen(["aplay", wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass
    def _send(self, code, body, typ):
        self.send_response(code)
        self.send_header("Content-Type", typ)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def do_GET(self):
        if self.path == "/face.jpg" and FACE.exists():
            self._send(200, FACE.read_bytes(), "image/jpeg")
        else:
            self._send(200, load_html(), "text/html; charset=utf-8")
    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        data = json.loads(self.rfile.read(n).decode() or "{}")
        if self.path == "/ask":
            body = json.dumps({"reply": ask(data.get("text", ""))}).encode()
        elif self.path == "/vault":
            group = data.get("group") or "Banking"
            title = data.get("title") or "Untitled"
            username = data.get("username") or ""
            secret = data.get("secret") or ""
            notes = data.get("notes") or "Entered through Destiny interface"
            if not secret:
                body = json.dumps({"ok": False, "reply": "Nothing to save."}).encode()
            else:
                p = subprocess.run(["python3", "/home/destiny/add_to_vault.py", group, title, username, secret, notes], capture_output=True, text=True, timeout=30)
                raw = (p.stdout or p.stderr or "").strip()
                body = json.dumps({"ok": p.returncode==0, "reply": raw or "Saved to vault."}).encode()
        elif self.path == "/mic":
            try:
                body = json.dumps({"ok": True, "text": listen()}).encode()
            except Exception as e:
                body = json.dumps({"ok": False, "text": "", "error": str(e)}).encode()
        elif self.path == "/speak":
            speak(data.get("text", ""))
            body = b'{"ok":true}'
        elif self.path == "/stop":
            subprocess.run(["pkill", "-f", "aplay"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            body = b'{"ok":true}'
        else:
            body = b'{}'
        self._send(200, body, "application/json")

print("CHAT ON  http://127.0.0.1:8765")
HTTPServer(("127.0.0.1", 8765), H).serve_forever()
