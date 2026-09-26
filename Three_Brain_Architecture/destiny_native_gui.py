import sys
import subprocess

try:
    import tkinter as tk
    from tkinter import scrolledtext, font
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])
    import tkinter as tk
    from tkinter import scrolledtext, font

class DestinyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Destiny - Next-Gen Interface")
        self.root.geometry("950x700")
        self.root.configure(bg="#1e1e1e")

        # Top Status Bar
        self.status_bar = tk.Label(root, text="DESTINY // SYSTEM ONLINE", bg="#252526", fg="#4ec9b0", font=("Helvetica", 11, "bold"), anchor="w", padx=15, pady=8)
        self.status_bar.pack(fill=tk.X)

        # Chat History Box (Fully selectable, copyable, scrollable)
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#f0f0f0", font=("Helvetica", 13), bd=0, highlightthickness=0, padx=15, pady=15)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_config("user", foreground="#ffffff", background="#007acc", lmargin1=10, lmargin2=10, rmargin=10, spacing1=5, spacing3=5)
        self.chat_display.tag_config("destiny", foreground="#f0f0f0", background="#2d2d2d", lmargin1=10, lmargin2=10, rmargin=10, spacing1=5, spacing3=5)
        self.chat_display.tag_config("system", foreground="#4ec9b0", font=("Helvetica", 11, "italic"))
        self.chat_display.config(state=tk.DISABLED)

        # Input Frame at the bottom
        input_frame = tk.Frame(root, bg="#252526", padx=15, pady=15)
        input_frame.pack(fill=tk.X)

        # Text input field
        self.entry_box = tk.Text(input_frame, height=3, bg="#333333", fg="#ffffff", font=("Helvetica", 13), bd=0, highlightthickness=0, wrap=tk.WORD)
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry_box.bind("<Return>", self.handle_return)
        self.entry_box.focus_set()

        # Send Button
        send_btn = tk.Button(input_frame, text="Send", command=self.send_message, bg="#007acc", fg="#ffffff", font=("Helvetica", 13, "bold"), bd=0, padx=20, relief=tk.FLAT, cursor="hand2")
        send_btn.pack(side=tk.RIGHT, fill=tk.Y)

        self.append_message("Destiny", "Hello Neil. I am fully online and connected. You can type, copy, and paste right here seamlessly.", "destiny")

    def append_message(self, sender, text, tag):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n{sender}:\n", "system")
        self.chat_display.insert(tk.END, f"{text}\n", tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def handle_return(self, event):
        # Allow shift+enter for new lines, enter to send
        if event.state & 0x0001: # Shift pressed
            return
        self.send_message()
        return "break"

    def send_message(self):
        msg = self.entry_box.get("1.0", tk.END).strip()
        if not msg:
            return
        self.entry_box.delete("1.0", tk.END)
        self.append_message("You", msg, "user")
        
        # Execute Destiny backend process directly
        try:
            result = subprocess.run(
                ["./destiny", msg],
                capture_output=True,
                text=True,
                cwd="/home/destiny/Obsidian/Destiny/Three_Brain_Architecture"
            )
            output = result.stdout.strip()
            if "=== RESULT ===" in output:
                reply = output.split("=== RESULT ===")[-1].strip()
            else:
                reply = output if output else "Task completed successfully."
        except Exception as e:
            reply = f"System Error: {e}"

        self.append_message("Destiny", reply, "destiny")

if __name__ == "__main__":
    root = tk.Tk()
    app = DestinyApp(root)
    root.mainloop()
