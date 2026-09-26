#!/usr/bin/env python3
import re, shutil, subprocess, tkinter as tk
from pathlib import Path

TASK = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/destiny_task.py")
FACE = Path("/home/destiny/Obsidian/Destiny/destiny_avatar.jpg")
FACE_PNG = Path("/tmp/destiny_face.png")

def which_voice():
    for n in ("espeak-ng", "espeak", "festival"):
        if shutil.which(n):
            return n
    return None

VOICE = which_voice()

def make_face():
    if FACE.exists():
        subprocess.run(["ffmpeg", "-y", "-i", str(FACE), "-vf", "scale=220:220", str(FACE_PNG)], capture_output=True)

def speak(text):
    if not VOICE or not text:
        return
    clean = re.sub(r"[=*`#]+", " ", text)
    clean = re.sub(r"\s+", " ", clean).strip()[:400]
    if VOICE == "festival":
        subprocess.Popen(["bash", "-lc", "echo " + repr(clean) + " | festival --tts"])
    else:
        subprocess.Popen([VOICE, "-s", "135", "-v", "en+f3", clean])

def ask(msg):
    p = subprocess.run(["python3", str(TASK), msg], capture_output=True, text=True, timeout=300)
    raw = (p.stdout or "") + (("\n" + p.stderr) if p.stderr else "")
    m = re.search(r"Destiny:\s*(.*?)(?:=== PIPELINE ===|DESTINY_TASK_COMPLETE|$)", raw, re.S)
    return (m.group(1).strip() if m else raw.strip()) or "No reply."

def send(_e=None):
    msg = box.get("1.0", "end").strip()
    if not msg:
        return
    out.delete("1.0", "end")
    out.insert("end", "Working...\n")
    root.update()
    try:
        text = ask(msg)
    except Exception as e:
        text = str(e)
    out.delete("1.0", "end")
    out.insert("end", text)
    speak(text)

make_face()
root = tk.Tk()
root.title("Destiny")
root.configure(bg="#0b0907")
root.geometry("1040x760")
bg, panel, gold, ink = "#0b0907", "#16110c", "#d7b56a", "#f3ead6"

head = tk.Frame(root, bg=panel)
head.pack(fill="x")
if FACE_PNG.exists():
    pic = tk.PhotoImage(file=str(FACE_PNG))
    lab = tk.Label(head, image=pic, bg=panel, bd=0)
    lab.image = pic
    lab.pack(side="left", padx=16, pady=14)

meta = tk.Frame(head, bg=panel)
meta.pack(side="left", fill="both", expand=True)
tk.Label(meta, text="DESTINY", fg=gold, bg=panel, font=("DejaVu Sans", 36, "bold")).pack(anchor="w", pady=(18, 0))
tk.Label(meta, text="ONLINE", fg="#8fbf6a", bg=panel, font=("DejaVu Sans", 13, "bold")).pack(anchor="w")

box = tk.Text(root, height=4, wrap="word", bg="#1b2418", fg=ink, insertbackground=ink, font=("DejaVu Sans", 17), relief="flat", padx=14, pady=12)
box.pack(fill="x", padx=18, pady=(16, 8))
box.focus_set()
box.bind("<Control-Return>", send)

row = tk.Frame(root, bg=bg)
row.pack()
tk.Button(row, text="Send", command=send, bg="#3b5c34", fg=ink, font=("DejaVu Sans", 16, "bold"), relief="flat", padx=22, pady=8).pack(side="left", padx=6)

def speak_again():
    speak(out.get("1.0", "end"))
tk.Button(row, text="Speak", command=speak_again, bg="#5a4630", fg=ink, font=("DejaVu Sans", 16, "bold"), relief="flat", padx=22, pady=8).pack(side="left", padx=6)

out = tk.Text(root, wrap="word", bg="#090807", fg=ink, font=("DejaVu Sans", 16), relief="flat", padx=14, pady=12)
out.pack(fill="both", expand=True, padx=18, pady=16)
out.insert("end", "Ready.")
root.mainloop()
