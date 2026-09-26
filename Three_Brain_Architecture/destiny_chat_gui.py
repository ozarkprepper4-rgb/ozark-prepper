import sys
import subprocess
try:
    import tkinter as tk
    from tkinter import scrolledtext, font
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])
    import tkinter as tk
    from tkinter import scrolledtext, font

class DestinyChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Destiny")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")

        # Custom fonts for easy reading
        self.chat_font = font.Font(family="Helvetica", size=14)
        self.entry_font = font.Font(family="Helvetica", size=14)

        # Chat history display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#ffffff", font=self.chat_font, bd=0, highlightthickness=0)
        self.chat_display.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)

        # Bottom frame for input
        input_frame = tk.Frame(root, bg="#2d2d2d")
        input_frame.pack(padx=15, pady=15, fill=tk.X)

        # Text input box
        self.entry_box = tk.Text(input_frame, height=2, bg="#333333", fg="#ffffff", font=self.entry_font, bd=0, highlightthickness=0, wrap=tk.WORD)
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry_box.bind("<Return>", self.handle_return)

        # Send button
        send_btn = tk.Button(input_frame, text="Send", command=self.send_message, bg="#007acc", fg="#ffffff", font=self.entry_font, bd=0, padx=15, relief=tk.FLAT)
        send_btn.pack(side=tk.RIGHT, fill=tk.Y)

        self.append_message("Destiny", "Hello Neil. I'm ready. Type your message below just like you do here.")

    def append_message(self, sender, text):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {text}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def handle_return(self, event):
        # Prevent default newline on enter, send instead
        self.send_message()
        return "break"

    def send_message(self):
        msg = self.entry_box.get("1.0", tk.END).strip()
        if not msg:
            return
        self.entry_box.delete("1.0", tk.END)
        self.append_message("You", msg)
        
        # Run through destiny backend
        try:
            result = subprocess.run(["./destiny", msg], capture_output=True, text=True, cwd="/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
            output = result.stdout.strip()
            # Extract result portion if formatted
            if "=== RESULT ===" in output:
                parts = output.split("=== RESULT ===")
                reply = parts[-1].strip()
            else:
                reply = output if output else "Done."
        except Exception as e:
            reply = f"Error communicating with backend: {e}"
            
        self.append_message("Destiny", reply)

if __name__ == "__main__":
    root = tk.Tk()
    app = DestinyChatApp(root)
    root.mainloop()
