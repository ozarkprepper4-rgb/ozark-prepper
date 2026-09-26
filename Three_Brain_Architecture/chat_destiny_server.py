#!/usr/bin/env python3

import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run

HOST = "127.0.0.1"
PORT = 8765

HTML = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Destiny</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#212121;color:#ececec;font-family:Arial,sans-serif;height:100vh;display:flex;flex-direction:column}
header{height:58px;border-bottom:1px solid #3a3a3a;display:flex;align-items:center;padding:0 22px;font-size:20px;font-weight:bold}
.status{margin-left:12px;font-size:12px;color:#4ade80;font-weight:normal}
#messages{flex:1;overflow-y:auto;padding:30px 18%;scroll-behavior:smooth}
.message{display:flex;margin:22px 0;line-height:1.55;font-size:16px}
.avatar{width:32px;height:32px;border-radius:50%;background:#8b5cf6;display:flex;align-items:center;justify-content:center;font-weight:bold;margin-right:14px;flex-shrink:0}
.user .avatar{background:#444}
.text{white-space:pre-wrap;max-width:850px}
#bottom{padding:15px 18% 25px}
#box{background:#2f2f2f;border:1px solid #555;border-radius:16px;padding:10px 12px;display:flex;align-items:flex-end}
textarea{flex:1;background:transparent;border:0;outline:0;color:#fff;resize:none;font:16px Arial;min-height:26px;max-height:180px;padding:8px}
button{border:0;border-radius:10px;padding:10px 14px;background:#8b5cf6;color:white;cursor:pointer;font-weight:bold}
button:hover{background:#7c3aed}
.attach{background:#444;margin-right:8px}
.copy{background:#444;margin-left:10px;font-size:11px}
.typing{color:#aaa;font-style:italic}
@media(max-width:800px){#messages,#bottom{padding-left:12px;padding-right:12px}}
</style>
</head>
<body>
<header>
DESTINY <span class="status">● ONLINE</span>
</header>

<div id="messages">
<div class="message">
<div class="avatar">D</div>
<div class="text">Hello, Neil. I am Destiny. I am connected to my existing Three-Brain system and ready to talk.</div>
</div>
</div>

<div id="bottom">
<div id="box">
<button class="attach" onclick="attach()">📎</button>
<textarea id="input" rows="1" placeholder="Message Destiny..."></textarea>
<button onclick="send()">↑</button>
</div>
</div>

<input id="file" type="file" hidden>

<script>
const input=document.getElementById("input");
const messages=document.getElementById("messages");

input.addEventListener("keydown",e=>{
    if(e.key==="Enter" && !e.shiftKey){
        e.preventDefault();
        send();
    }
});

input.addEventListener("input",()=>{
    input.style.height="auto";
    input.style.height=Math.min(input.scrollHeight,180)+"px";
});

async function send(){
    const text=input.value.trim();
    if(!text)return;

    add("N",text,true);
    input.value="";
    input.style.height="auto";

    const thinking=add("D","Thinking...",false,true);

    try{
        const response=await fetch("/api/chat",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({message:text})
        });

        const data=await response.json();
        thinking.remove();

        add("D",data.response || ("ERROR: "+data.error),false);
    }catch(e){
        thinking.remove();
        add("D","Connection error: "+e,false);
    }
}

function add(letter,text,user,typing=false){
    const row=document.createElement("div");
    row.className="message";
    if(user)row.classList.add("user");

    const avatar=document.createElement("div");
    avatar.className="avatar";
    avatar.textContent=letter;

    const body=document.createElement("div");
    body.className="text";
    if(typing)body.className+=" typing";
    body.textContent=text;

    row.appendChild(avatar);
    row.appendChild(body);

    if(!typing){
        const copy=document.createElement("button");
        copy.className="copy";
        copy.textContent="Copy";
        copy.onclick=()=>{
            navigator.clipboard.writeText(text);
            copy.textContent="Copied";
            setTimeout(()=>copy.textContent="Copy",1200);
        };
        row.appendChild(copy);
    }

    messages.appendChild(row);
    messages.scrollTop=messages.scrollHeight;
    return row;
}

function attach(){
    document.getElementById("file").click();
}

document.getElementById("file").addEventListener("change",e=>{
    const file=e.target.files[0];
    if(!file)return;

    input.value+="\nI have given you this file: "+file.name;
    input.focus();
});
</script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == "/" or self.path == "/chat":
            data=HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.send_header("Content-Length",str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        self.send_error(404)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return

        try:
            length=int(self.headers.get("Content-Length",0))
            body=self.rfile.read(length)
            request=json.loads(body.decode("utf-8"))
            task=request.get("message","").strip()

            if not task:
                raise ValueError("Empty message.")

            result=run(task)
            response=result.get("model_response","No response returned.")

            output={"response":response}

        except Exception as exc:
            output={"error":str(exc)}

        data=json.dumps(output).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    server=ThreadingHTTPServer((HOST,PORT),Handler)
    print("DESTINY CHAT ONLINE")
    print(f"http://{HOST}:{PORT}")

    threading.Thread(
        target=lambda:webbrowser.open(f"http://{HOST}:{PORT}"),
        daemon=True
    ).start()

    server.serve_forever()


if __name__=="__main__":
    main()
