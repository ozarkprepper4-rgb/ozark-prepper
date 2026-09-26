import subprocess
#!/usr/bin/env python3

import tkinter as tk
from tkinter import scrolledtext
import threading
import sys
from pathlib import Path
from datetime import datetime

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run
from destiny_ptt import record_command, transcribe, speak


class DestinyJarvis:
    BG = "#07111f"
    PANEL = "#0b1b2b"
    PANEL2 = "#10283d"
    BORDER = "#164a67"
    CYAN = "#42d9ff"
    BLUE = "#2196f3"
    TEXT = "#e9f6ff"
    MUTED = "#7fa6ba"
    GREEN = "#5cff9d"
    YELLOW = "#ffd166"
    RED = "#ff6577"

    def __init__(self, root):
        self.root = root
        self.busy = False

        root.title("DESTINY // Cognitive Operations Interface")
        root.geometry("1400x900")
        root.minsize(1100, 700)
        root.configure(bg=self.BG)

        self.build_header()
        self.build_body()
        self.build_footer()
        self.last_destiny_response = ""
        self.root.after(150, self.install_compact_voice_controls)


        self.update_clock()
        self.refresh_system_status()
        self.animate_core()

        self.add_chat(
            "DESTINY",
            "Hello. Destiny cognitive interface online."
        )

        self.add_activity("Interface initialized.")
        self.add_activity("Three-Brain orchestrator connected.")

        self.input.focus_set()

    # ---------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------

    def build_header(self):
        header = tk.Frame(
            self.root,
            bg=self.PANEL,
            height=80,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        left = tk.Frame(header, bg=self.PANEL)
        left.pack(side=tk.LEFT, padx=22)

        tk.Label(
            left,
            text="DESTINY",
            font=("DejaVu Sans", 26, "bold"),
            fg=self.CYAN,
            bg=self.PANEL
        ).pack(anchor="w")

        tk.Label(
            left,
            text="COGNITIVE OPERATIONS INTERFACE",
            font=("DejaVu Sans", 9, "bold"),
            fg=self.MUTED,
            bg=self.PANEL
        ).pack(anchor="w")

        center = tk.Frame(header, bg=self.PANEL)
        center.pack(side=tk.LEFT, expand=True)

        self.core_canvas = tk.Canvas(
            center,
            width=80,
            height=70,
            bg=self.PANEL,
            highlightthickness=0
        )
        self.core_canvas.pack()

        right = tk.Frame(header, bg=self.PANEL)
        right.pack(side=tk.RIGHT, padx=22)

        self.clock_label = tk.Label(
            right,
            text="",
            font=("DejaVu Sans Mono", 14, "bold"),
            fg=self.TEXT,
            bg=self.PANEL
        )
        self.clock_label.pack(anchor="e")

        self.master_status = tk.Label(
            right,
            text="SYSTEM ONLINE",
            font=("DejaVu Sans", 9, "bold"),
            fg=self.GREEN,
            bg=self.PANEL
        )
        self.master_status.pack(anchor="e")

    # ---------------------------------------------------------
    # MAIN BODY
    # ---------------------------------------------------------

    def build_body(self):
        body = tk.Frame(self.root, bg=self.BG)
        body.pack(fill=tk.BOTH, expand=True, padx=14, pady=14)

        self.build_sidebar(body)
        self.build_chat_panel(body)
        self.build_activity_panel(body)

    def build_sidebar(self, parent):
        sidebar = tk.Frame(
            parent,
            bg=self.PANEL,
            width=215,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="THREE-BRAIN STATUS",
            bg=self.PANEL,
            fg=self.CYAN,
            font=("DejaVu Sans", 11, "bold")
        ).pack(pady=(20, 15))

        self.brain_labels = {}

        for name in [
            "DEEP LEARNING",
            "MACHINE LEARNING",
            "ADAPTIVE BRAIN",
            "COGNITIVE CORE"
        ]:
            card = tk.Frame(
                sidebar,
                bg=self.PANEL2,
                highlightbackground=self.BORDER,
                highlightthickness=1
            )
            card.pack(fill=tk.X, padx=12, pady=6)

            tk.Label(
                card,
                text=name,
                bg=self.PANEL2,
                fg=self.MUTED,
                font=("DejaVu Sans", 9, "bold")
            ).pack(anchor="w", padx=10, pady=(8, 1))

            status = tk.Label(
                card,
                text="● ONLINE",
                bg=self.PANEL2,
                fg=self.GREEN,
                font=("DejaVu Sans Mono", 9, "bold")
            )
            status.pack(anchor="w", padx=10, pady=(1, 8))

            self.brain_labels[name] = status

        tk.Label(
            sidebar,
            text="SYSTEM",
            bg=self.PANEL,
            fg=self.CYAN,
            font=("DejaVu Sans", 10, "bold")
        ).pack(pady=(25, 8))

        self.task_count_label = tk.Label(
            sidebar,
            text="Tasks this session: 0",
            bg=self.PANEL,
            fg=self.TEXT,
            font=("DejaVu Sans", 9)
        )
        self.task_count_label.pack()

        self.task_count = 0

        tk.Button(
            sidebar,
            text="CLEAR CHAT",
            command=self.clear_chat,
            bg=self.PANEL2,
            fg=self.TEXT,
            activebackground=self.BORDER,
            activeforeground=self.TEXT,
            relief=tk.FLAT,
            font=("DejaVu Sans", 9, "bold")
        ).pack(fill=tk.X, padx=12, pady=(30, 5))

        tk.Button(
            sidebar,
            text="REFRESH STATUS",
            command=self.refresh_system_status,
            bg=self.PANEL2,
            fg=self.TEXT,
            activebackground=self.BORDER,
            activeforeground=self.TEXT,
            relief=tk.FLAT,
            font=("DejaVu Sans", 9, "bold")
        ).pack(fill=tk.X, padx=12, pady=5)

    def build_chat_panel(self, parent):
        center = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        center.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=(0, 12)
        )

        titlebar = tk.Frame(center, bg=self.PANEL2, height=42)
        titlebar.pack(fill=tk.X)
        titlebar.pack_propagate(False)

        tk.Label(
            titlebar,
            text="LIVE COMMUNICATION",
            bg=self.PANEL2,
            fg=self.CYAN,
            font=("DejaVu Sans", 10, "bold")
        ).pack(side=tk.LEFT, padx=14)

        self.task_status = tk.Label(
            titlebar,
            text="READY",
            bg=self.PANEL2,
            fg=self.GREEN,
            font=("DejaVu Sans Mono", 9, "bold")
        )
        self.task_status.pack(side=tk.RIGHT, padx=14)

        self.chat = scrolledtext.ScrolledText(
            center,
            wrap=tk.WORD,
            bg=self.BG,
            fg=self.TEXT,
            insertbackground=self.CYAN,
            font=("DejaVu Sans", 12),
            padx=18,
            pady=18,
            relief=tk.FLAT,
            selectbackground=self.BLUE
        )
        self.chat.pack(fill=tk.BOTH, expand=True)
        self.chat.config(state=tk.DISABLED)

        self.chat.tag_config(
            "destiny",
            foreground=self.CYAN,
            font=("DejaVu Sans", 11, "bold")
        )

        self.chat.tag_config(
            "neil",
            foreground=self.GREEN,
            font=("DejaVu Sans", 11, "bold")
        )

        self.chat.tag_config(
            "system",
            foreground=self.YELLOW
        )

        input_frame = tk.Frame(center, bg=self.PANEL2)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.input = tk.Text(
            input_frame,
            height=3,
            wrap=tk.WORD,
            bg=self.BG,
            fg=self.TEXT,
            insertbackground=self.CYAN,
            font=("DejaVu Sans", 12),
            relief=tk.FLAT,
            padx=12,
            pady=10,
            selectbackground=self.BLUE
        )
        self.input.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=(0, 10)
        )

        self.input.bind("<Return>", self.enter_pressed)
        self.input.bind("<Control-Return>", self.ctrl_enter_pressed)

        self.send_button = tk.Button(
            input_frame,
            text="SEND",
            command=self.send,
            bg=self.CYAN,
            fg="#001018",
            activebackground="#8aeaff",
            relief=tk.FLAT,
            font=("DejaVu Sans", 10, "bold"),
            padx=24
        )
        self.send_button.pack(side=tk.RIGHT, fill=tk.Y)

        self.install_context_menu(self.input, editable=True)
        self.install_context_menu(self.chat, editable=False)

    def build_activity_panel(self, parent):
        right = tk.Frame(
            parent,
            bg=self.PANEL,
            width=280,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        right.pack(side=tk.RIGHT, fill=tk.Y)
        right.pack_propagate(False)

        tk.Label(
            right,
            text="ACTIVITY STREAM",
            bg=self.PANEL2,
            fg=self.CYAN,
            font=("DejaVu Sans", 10, "bold"),
            pady=12
        ).pack(fill=tk.X)

        self.activity = scrolledtext.ScrolledText(
            right,
            wrap=tk.WORD,
            bg=self.PANEL,
            fg=self.MUTED,
            font=("DejaVu Sans Mono", 9),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.activity.pack(fill=tk.BOTH, expand=True)
        self.activity.config(state=tk.DISABLED)

        self.install_context_menu(self.activity, editable=False)

    # ---------------------------------------------------------
    # FOOTER
    # ---------------------------------------------------------

    def build_footer(self):
        footer = tk.Frame(
            self.root,
            bg=self.PANEL,
            height=30
        )
        footer.pack(fill=tk.X)
        footer.pack_propagate(False)

        tk.Label(
            footer,
            text="DESTINY // LOCAL COGNITIVE SYSTEM",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("DejaVu Sans Mono", 8)
        ).pack(side=tk.LEFT, padx=12)

        tk.Label(
            footer,
            text="Three-Brain Architecture",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("DejaVu Sans Mono", 8)
        ).pack(side=tk.RIGHT, padx=12)

    # ---------------------------------------------------------
    # CHAT
    # ---------------------------------------------------------

    def add_chat(self, speaker, text):
        self.chat.config(state=tk.NORMAL)

        timestamp = datetime.now().strftime("%H:%M:%S")

        tag = "destiny" if speaker == "DESTINY" else "neil"

        self.chat.insert(
            tk.END,
            f"[{timestamp}] {speaker}\n",
            tag
        )

        self.chat.insert(
            tk.END,
            f"{text}\n\n"
        )

        self.chat.see(tk.END)
        self.chat.config(state=tk.DISABLED)

    def send(self):
        if self.busy:
            return

        message = self.input.get("1.0", tk.END).strip()

        if not message:
            return

        self.input.delete("1.0", tk.END)

        self.add_chat("NEIL", message)

        self.busy = True
        self.task_count += 1

        self.task_count_label.config(
            text=f"Tasks this session: {self.task_count}"
        )

        self.task_status.config(
            text="PROCESSING",
            fg=self.YELLOW
        )

        self.send_button.config(
            state=tk.DISABLED,
            text="WORKING"
        )

        self.add_activity(
            "Task received: " + message[:65]
        )

        threading.Thread(
            target=self.get_response,
            args=(message,),
            daemon=True
        ).start()

    def get_response(self, message):
        try:
            result = run(message)

            if isinstance(result, dict):
                response = result.get("model_response")

                if not response:
                    response = result.get("message")

                if not response:
                    response = str(result)

                status = result.get("status", "UNKNOWN")
            else:
                response = str(result)
                status = "UNKNOWN"

        except Exception as e:
            response = f"System error: {e}"
            status = "FAIL"

        self.root.after(
            0,
            lambda: self.finish_response(
                response,
                status
            )
        )

    def finish_response(self, response, status):
        self.last_destiny_response = str(response)

        self.add_chat("DESTINY", response)

        if status == "PASS":
            color = self.GREEN
        elif status == "FAIL":
            color = self.RED
        else:
            color = self.YELLOW

        self.task_status.config(
            text=status,
            fg=color
        )

        self.add_activity(
            f"Task completed with status: {status}"
        )

        self.send_button.config(
            state=tk.NORMAL,
            text="SEND"
        )

        self.busy = False
        self.input.focus_set()


    def install_compact_voice_controls(self):
        """
        Three compact controls only:

        1. MIC beside SEND:
           speech -> typing box, but DOES NOT send.

        2. STOP beside SEND:
           immediately stops Destiny speaking.

        3. REPLAY beside conversation:
           speaks Destiny's last answer again.
        """

        # -------------------------------
        # MIC + STOP beside SEND
        # -------------------------------

        send_parent = self.send_button.master

        self.dictate_button = tk.Button(
            send_parent,
            text="🎙",
            command=self.dictate_to_input,
            bg="#10394a",
            fg="#00e5ff",
            activebackground="#00e5ff",
            activeforeground="#001219",
            font=("Arial", 14, "bold"),
            relief="flat",
            width=3,
            cursor="hand2"
        )

        self.stop_voice_button = tk.Button(
            send_parent,
            text="■",
            command=self.stop_destiny_voice,
            bg="#5a1d2c",
            fg="#ff8da1",
            activebackground="#ff4567",
            activeforeground="white",
            font=("Arial", 13, "bold"),
            relief="flat",
            width=3,
            cursor="hand2"
        )

        manager = self.send_button.winfo_manager()

        if manager == "pack":
            self.stop_voice_button.pack(
                side="right",
                padx=(3, 3),
                pady=2,
                before=self.send_button
            )

            self.dictate_button.pack(
                side="right",
                padx=(3, 3),
                pady=2,
                before=self.stop_voice_button
            )

        elif manager == "grid":
            info = self.send_button.grid_info()

            row = int(info.get("row", 0))
            col = int(info.get("column", 0))

            # Move SEND right enough to make room.
            self.send_button.grid_configure(
                column=col + 2
            )

            self.dictate_button.grid(
                row=row,
                column=col,
                padx=3,
                pady=2
            )

            self.stop_voice_button.grid(
                row=row,
                column=col + 1,
                padx=3,
                pady=2
            )

        else:
            # Fallback for a placed SEND button.
            self.dictate_button.place(
                relx=0.72,
                rely=0.5,
                anchor="center",
                width=42,
                height=38
            )

            self.stop_voice_button.place(
                relx=0.79,
                rely=0.5,
                anchor="center",
                width=42,
                height=38
            )


        # -------------------------------
        # Find Destiny's conversation box
        # -------------------------------

        chat_widget = self._find_chat_display_widget()

        if chat_widget is not None:
            chat_parent = chat_widget.master

            self.replay_voice_button = tk.Button(
                chat_parent,
                text="🎙  REPLAY",
                command=self.replay_destiny_voice,
                bg="#102a3c",
                fg="#00e5ff",
                activebackground="#00e5ff",
                activeforeground="#001219",
                font=("Arial", 9, "bold"),
                relief="flat",
                padx=8,
                pady=4,
                cursor="hand2"
            )

            # Small button at upper-right of Destiny's conversation area.
            self.replay_voice_button.place(
                relx=0.985,
                y=8,
                anchor="ne"
            )

            self.replay_voice_button.lift()


    def _walk_widgets(self, parent):
        result = []

        for child in parent.winfo_children():
            result.append(child)
            result.extend(
                self._walk_widgets(child)
            )

        return result


    def _find_input_widget(self):
        """
        Locate the editable typing widget associated with SEND.
        """

        # First search around SEND.
        node = self.send_button.master

        for _ in range(4):
            for widget in self._walk_widgets(node):
                try:
                    cls = widget.winfo_class()
                    state = str(widget.cget("state"))

                    if (
                        cls in ("Text", "Entry", "TEntry")
                        and state != "disabled"
                    ):
                        return widget

                except Exception:
                    pass

            try:
                node = node.master
            except Exception:
                break

        # Final fallback: whole application.
        for widget in self._walk_widgets(self.root):
            try:
                cls = widget.winfo_class()
                state = str(widget.cget("state"))

                if (
                    cls in ("Text", "Entry", "TEntry")
                    and state != "disabled"
                ):
                    return widget

            except Exception:
                pass

        return None


    def _find_chat_display_widget(self):
        """
        Locate the main conversation display.
        """

        candidates = []

        for widget in self._walk_widgets(self.root):
            try:
                cls = widget.winfo_class()

                if cls == "Text":
                    height = widget.winfo_height()
                    candidates.append(
                        (height, widget)
                    )

            except Exception:
                pass

        if not candidates:
            return None

        # The main conversation widget is normally the tallest Text widget.
        candidates.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return candidates[0][1]


    # ============================================================
    # MIC BESIDE SEND
    # ============================================================

    def dictate_to_input(self):
        """
        Listen to Neil and put the transcription into the typing box.
        DO NOT send it automatically.
        """

        if getattr(self, "_dictating", False):
            return

        self._dictating = True

        self.dictate_button.configure(
            text="●",
            fg="#ff4567",
            state="disabled"
        )

        self.add_activity(
            "MIC: Listening..."
        )

        threading.Thread(
            target=self._dictation_worker,
            daemon=True
        ).start()


    def _dictation_worker(self):
        try:
            audio = record_command()

            if audio is None:
                self.root.after(
                    0,
                    lambda: self._finish_dictation("")
                )
                return

            text = transcribe(audio)

            self.root.after(
                0,
                lambda t=text: self._finish_dictation(t)
            )

        except Exception as exc:
            error = str(exc)

            self.root.after(
                0,
                lambda e=error: self._dictation_error(e)
            )


    def _finish_dictation(self, text):
        self._dictating = False

        self.dictate_button.configure(
            text="🎙",
            fg="#00e5ff",
            state="normal"
        )

        if not text:
            self.add_activity(
                "MIC: Nothing detected"
            )
            return

        widget = self._find_input_widget()

        if widget is None:
            self.add_activity(
                "MIC ERROR: typing box not found"
            )
            return

        try:
            cls = widget.winfo_class()

            if cls == "Text":
                existing = widget.get(
                    "1.0",
                    "end-1c"
                ).strip()

                if existing:
                    widget.insert(
                        "end",
                        " " + text
                    )
                else:
                    widget.insert(
                        "end",
                        text
                    )

                widget.see("end")

            else:
                existing = widget.get().strip()

                if existing:
                    widget.insert(
                        "end",
                        " " + text
                    )
                else:
                    widget.insert(
                        "end",
                        text
                    )

            widget.focus_set()

            self.add_activity(
                "MIC: Speech placed in message box"
            )

        except Exception as exc:
            self.add_activity(
                "MIC ERROR: " + str(exc)
            )


    def _dictation_error(self, error):
        self._dictating = False

        self.dictate_button.configure(
            text="🎙",
            fg="#00e5ff",
            state="normal"
        )

        self.add_activity(
            "MIC ERROR: " + error
        )


    # ============================================================
    # STOP DESTINY SPEAKING
    # ============================================================

    def stop_destiny_voice(self):
        subprocess.run(
            ["pkill", "-f", "aplay"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )

        subprocess.run(
            ["pkill", "-f", "piper"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )

        self.add_activity(
            "VOICE: Speech stopped"
        )


    # ============================================================
    # REPLAY DESTINY'S LAST ANSWER
    # ============================================================

    def replay_destiny_voice(self):
        text = getattr(
            self,
            "last_destiny_response",
            ""
        ).strip()

        if not text:
            self.add_activity(
                "VOICE: No Destiny response to replay"
            )
            return

        self.add_activity(
            "VOICE: Replaying Destiny's last response"
        )

        threading.Thread(
            target=self._replay_worker,
            args=(text,),
            daemon=True
        ).start()


    def _replay_worker(self, text):
        try:
            speak(text)

        except Exception as exc:
            error = str(exc)

            self.root.after(
                0,
                lambda e=error: self.add_activity(
                    "VOICE ERROR: " + e
                )
            )


    def clear_chat(self):
        self.chat.config(state=tk.NORMAL)
        self.chat.delete("1.0", tk.END)
        self.chat.config(state=tk.DISABLED)

        self.add_chat(
            "DESTINY",
            "Communication display cleared."
        )

    # ---------------------------------------------------------
    # KEYBOARD / CLIPBOARD
    # ---------------------------------------------------------

    def enter_pressed(self, event):
        if event.state & 0x0001:
            return None

        self.send()
        return "break"

    def ctrl_enter_pressed(self, event):
        self.send()
        return "break"

    def install_context_menu(self, widget, editable):
        menu = tk.Menu(
            self.root,
            tearoff=0,
            bg=self.PANEL2,
            fg=self.TEXT
        )

        menu.add_command(
            label="Copy",
            command=lambda: self.copy_selection(widget)
        )

        if editable:
            menu.add_command(
                label="Paste",
                command=lambda: widget.event_generate("<<Paste>>")
            )

            menu.add_command(
                label="Cut",
                command=lambda: widget.event_generate("<<Cut>>")
            )

        menu.add_separator()

        menu.add_command(
            label="Select All",
            command=lambda: self.select_all(widget)
        )

        def popup(event):
            menu.tk_popup(event.x_root, event.y_root)

        widget.bind("<Button-3>", popup)

        widget.bind(
            "<Control-c>",
            lambda e: self.copy_selection(widget)
        )

        if editable:
            widget.bind(
                "<Control-v>",
                lambda e: widget.event_generate("<<Paste>>")
            )

            widget.bind(
                "<Control-x>",
                lambda e: widget.event_generate("<<Cut>>")
            )

        widget.bind(
            "<Control-a>",
            lambda e: self.select_all(widget)
        )

    def copy_selection(self, widget):
        try:
            text = widget.get(
                tk.SEL_FIRST,
                tk.SEL_LAST
            )

            self.root.clipboard_clear()
            self.root.clipboard_append(text)

        except tk.TclError:
            pass

        return "break"

    def select_all(self, widget):
        try:
            widget.tag_add(
                tk.SEL,
                "1.0",
                tk.END
            )
        except Exception:
            pass

        return "break"

    # ---------------------------------------------------------
    # ACTIVITY
    # ---------------------------------------------------------

    def add_activity(self, text):
        self.activity.config(state=tk.NORMAL)

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.activity.insert(
            tk.END,
            f"{timestamp}  {text}\n\n"
        )

        self.activity.see(tk.END)
        self.activity.config(state=tk.DISABLED)

    # ---------------------------------------------------------
    # SYSTEM STATUS
    # ---------------------------------------------------------

    def refresh_system_status(self):
        checks = {
            "DEEP LEARNING":
                BASE / "DL_Brain",

            "MACHINE LEARNING":
                BASE / "ML_Brain",

            "ADAPTIVE BRAIN":
                BASE / "Adaptive_Brain",

            "COGNITIVE CORE":
                BASE / "cognitive_orchestrator.py"
        }

        all_online = True

        for name, path in checks.items():
            online = path.exists()

            self.brain_labels[name].config(
                text="● ONLINE" if online else "● OFFLINE",
                fg=self.GREEN if online else self.RED
            )

            if not online:
                all_online = False

        self.master_status.config(
            text="SYSTEM ONLINE"
            if all_online
            else "SYSTEM DEGRADED",

            fg=self.GREEN
            if all_online
            else self.RED
        )

    # ---------------------------------------------------------
    # CLOCK / ANIMATED CORE
    # ---------------------------------------------------------

    def update_clock(self):
        self.clock_label.config(
            text=datetime.now().strftime(
                "%Y-%m-%d  %H:%M:%S"
            )
        )

        self.root.after(
            1000,
            self.update_clock
        )

    def animate_core(self):
        self.core_canvas.delete("all")

        t = datetime.now().microsecond // 100000

        pulse = 3 if t % 2 == 0 else 0

        self.core_canvas.create_oval(
            15 - pulse,
            10 - pulse,
            65 + pulse,
            60 + pulse,
            outline=self.BORDER,
            width=2
        )

        self.core_canvas.create_oval(
            23,
            18,
            57,
            52,
            outline=self.CYAN,
            width=2
        )

        self.core_canvas.create_oval(
            32,
            27,
            48,
            43,
            fill=self.CYAN,
            outline=""
        )

        self.root.after(
            150,
            self.animate_core
        )



# ============================================================
# DESTINY REPLY SPEAKER BUTTON
# ============================================================

_original_destiny_add_chat = DestinyJarvis.add_chat


def _destiny_add_chat_with_speaker(self, speaker, text):
    # Let the existing interface display the message normally.
    _original_destiny_add_chat(self, speaker, text)

    if str(speaker).upper() != "DESTINY":
        return

    spoken_text = str(text).strip()

    if not spoken_text:
        return

    # Find the main chat Text widget.
    def walk(widget):
        items = []

        for child in widget.winfo_children():
            items.append(child)
            items.extend(walk(child))

        return items

    candidates = []

    for widget in walk(self.root):
        try:
            if widget.winfo_class() == "Text":
                candidates.append(
                    (
                        widget.winfo_width() * widget.winfo_height(),
                        widget
                    )
                )
        except Exception:
            pass

    if not candidates:
        return

    candidates.sort(
        key=lambda item: item[0],
        reverse=True
    )

    chat = candidates[0][1]

    # Temporarily make editable if the chat widget is read-only.
    try:
        old_state = str(chat.cget("state"))
    except Exception:
        old_state = "normal"

    try:
        if old_state == "disabled":
            chat.configure(state="normal")

        button = tk.Button(
            chat,
            text="🔊  HEAR AGAIN",
            command=lambda t=spoken_text: threading.Thread(
                target=speak,
                args=(t,),
                daemon=True
            ).start(),
            bg="#10394a",
            fg="#00e5ff",
            activebackground="#00e5ff",
            activeforeground="#001219",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=3
        )

        # Put the button INSIDE the chat immediately after Destiny's reply.
        chat.insert("end", "   ")
        chat.window_create(
            "end",
            window=button
        )
        chat.insert("end", "\n\n")
        chat.see("end")

    finally:
        if old_state == "disabled":
            chat.configure(state="disabled")


DestinyJarvis.add_chat = _destiny_add_chat_with_speaker


def main():
    root = tk.Tk()

    DestinyJarvis(root)

    root.mainloop()


if __name__ == "__main__":
    main()
