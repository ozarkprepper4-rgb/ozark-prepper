import sys
import subprocess
import threading
try:
    import webview
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywebview"])
    import webview

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Destiny</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        #chat-container {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .message {
            padding: 12px 16px;
            border-radius: 8px;
            max-width: 85%;
            line-height: 1.5;
            font-size: 16px;
            word-wrap: break-word;
            user-select: text;
            -webkit-user-select: text;
        }
        .user {
            background-color: #007acc;
            align-self: flex-end;
        }
        .destiny {
            background-color: #2d2d2d;
            align-self: flex-start;
        }
        #input-container {
            padding: 15px;
            background-color: #252526;
            display: flex;
            gap: 10px;
            border-top: 1px solid #333333;
        }
        textarea {
            flex: 1;
            background-color: #333333;
            color: #ffffff;
            border: none;
            border-radius: 6px;
            padding: 12px;
            font-size: 16px;
            font-family: inherit;
            resize: none;
            height: 24px;
            outline: none;
        }
        button {
            background-color: #007acc;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0 20px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #005999;
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <div class="message destiny">Hello Neil. I'm ready. You can type, copy, and paste right here just like your main window.</div>
    </div>
    <div id="input-container">
        <textarea id="user-input" placeholder="Type a message..." autofocus></textarea>
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

            const reply = await window.pywebview.api.send_to_destiny(text);
            appendMessage('Destiny', reply);
        }
    </script>
</body>
</html>
"""

class Api:
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
            return output if output else "Done."
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    api = Api()
    window = webview.create_window("Destiny", html=HTML_CONTENT, js_api=api, width=900, height=700)
    webview.start()
