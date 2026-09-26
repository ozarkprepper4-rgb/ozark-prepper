#!/usr/bin/env python3
import tkinter as tk
from tkinter import scrolledtext
import threading
import sys
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run


class DestinyChat:
    def __init__(self, root):
        self.root = root
        root.title("Destiny")
        root.geometry("1000x750")

        self.chat = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 13),
            bg="#212121",
            fg="#eeeeee",
            insertbackground="white",
            padx=20,
            pady=20
        )
        self.chat.pack(fill=tk.BOTH, expand=True)

        self.chat.insert(
            tk.END,
            "Destiny: Hello Neil. I am ready.\n\n"
        )
        self.chat.config(state=tk.DISABLED)

        bottom = tk.Frame(root, bg="#212121")
        bottom.pack(fill=tk.X, padx=15, pady=15)

        self.entry = tk.Entry(
            bottom,
            font=("Arial", 14),
            bg="#303030",
            fg="white",
            insertbackground="white"
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)
        self.entry.bind("<Return>", lambda e: self.send())
        self.entry.focus()

        tk.Button(
            bottom,
            text="Send",
            command=self.send,
            font=("Arial", 12, "bold"),
            padx=20,
            pady=8
        ).pack(side=tk.RIGHT, padx=(10, 0))

    def add_message(self, speaker, text):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(tk.END, f"{speaker}: {text}\n\n")
        self.chat.see(tk.END)
        self.chat.config(state=tk.DISABLED)

    def send(self):
        message = self.entry.get().strip()
        if not message:
            return

        self.entry.delete(0, tk.END)
        self.add_message("Neil", message)
        self.add_message("Destiny", "Thinking...")

        threading.Thread(
            target=self.get_response,
            args=(message,),
            daemon=True
        ).start()

    def get_response(self, message):
        try:
            result = run(message)
            response = result.get(
                "model_response",
                "I did not receive a response."
            )
        except Exception as e:
            response = f"Error connecting to Destiny: {e}"

        self.root.after(
            0,
            lambda: self.replace_thinking(response)
        )

    def replace_thinking(self, response):
        self.chat.config(state=tk.NORMAL)

        content = self.chat.get("1.0", tk.END)
        marker = "Destiny: Thinking...\n\n"

        if marker in content:
            start = content.rfind(marker)
            self.chat.delete(f"1.0+{start}c", tk.END)
            self.chat.insert(tk.END, f"Destiny: {response}\n\n")
        else:
            self.chat.insert(tk.END, f"Destiny: {response}\n\n")

        self.chat.see(tk.END)
        self.chat.config(state=tk.DISABLED)


root = tk.Tk()
DestinyChat(root)
root.mainloop()
