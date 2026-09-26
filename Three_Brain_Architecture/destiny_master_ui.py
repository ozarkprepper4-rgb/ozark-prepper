import sys
import subprocess
try:
    import webview
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywebview"])
    import webview

HTML_UI = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Destiny - Master Interface</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: #f0f0f0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        #header {
            background-color: #252526;
            padding: 12px 20px;
            font-size: 14px;
            font-weight: bold;
            color: #4ec9b0;
            border-bottom: 1px solid #333333;
            letter-spacing: 0.5px;
        }
        #chat-container {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .message {
            padding: 14px 18px;
            border-radius: 8px;
            max-width: 85%;
            line-height: 1.6;
            font-size: 15px;
            word-wrap: break-word;
            user-select: text;
            -webkit-user-select: text;
        }
        .user {
            background-color: #007acc;
            color: #ffffff;
            align-self: flex-end;
        }
        .destiny {
            background-color: #2d2d2d;
            color: #f0f0f0;
            align-self: flex-start;
            border-left: 4px solid #4ec9b0;
        }
        #input-container {
            padding: 15px;
            background-color: #252526;
            display: flex;
            gap: 12px;
            border-top: 1px solid #333333;
        }
        textarea {
            flex: 1;
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 12px;
            font-size: 15px;
            font-family: inherit;
            resize: none;
            height: 28px;
            outline: none;
        }
        textarea:focus {
            border-color: #007acc;
        }
        button {
            background-color: #007acc;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0 24px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            background-color: #005999;
        }
    </style>
</head>
<body>
    <div id="header">DESTINY // THREE-BRAIN ACTIVE INTERFACE</div>
    <div id="chat-container">
        <div class="message destiny">Hello Neil. I am fully online, connected to my core architecture, and ready. You can type, copy, and paste right here seamlessly.</div>
    </div>
    <div id="input-container">
        <textarea id="user-input" placeholder="Message Destiny..." autofocus></textarea>
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const input = document.getElementById('user-input');
        const container = document.getElementById('chat-container');

        input.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        function appendMessage(sender, text) {
            const div = document.createElement('div');
            div.className = 'message ' + (sender === 'You' ? 'user' : 'destiny');
            div.innerText = text;
            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        }

        async function sendMessage() {
            const text = input.value.trim();
            if (!text) return;
            input.value = '';
            appendMessage('You', text);

            try {
                const reply = await window.pywebview.api.send_to_destiny(text);
                appendMessage('Destiny', reply);
            } catch (err) {
                appendMessage('Destiny', 'Error communicating with core backend.');
            }
        }
    </script>
</body>
</html>
"""

class DestinyAPI:
    def send_to_destiny(self, message):
        try:
            result = subprocess.run(
                ["./destiny", message],
                capture_output=True,
                text=True,
                cwd="/home/destiny/Obsidian/Destiny/Three_Brain_Architecture"
            )
            output = result.stdout.strip()
            if "=== RESULT ===" in output:
                return output.split("=== RESULT ===")[-1].strip()
            return output if output else "Task processed successfully."
        except Exception as e:
            return f"Execution Error: {e}"

if __name__ == '__main__':
    api = DestinyAPI()
    window = webview.create_window("Destiny", html=HTML_UI, js_api=api, width=1000, height=750)
    webview.start()
