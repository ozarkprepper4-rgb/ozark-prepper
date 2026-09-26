#!/bin/bash
cd /home/destiny/Obsidian/Destiny/Three_Brain_Architecture
if ! curl -s http://127.0.0.1:8765 >/dev/null; then
  python3 /home/destiny/Obsidian/Destiny/Three_Brain_Architecture/destiny_chat_server.py >/tmp/destiny_chat.log 2>&1 &
  sleep 1
fi
google-chrome --app=http://127.0.0.1:8765 >/tmp/destiny_chrome.log 2>&1 &
