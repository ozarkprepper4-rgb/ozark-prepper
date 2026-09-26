#!/bin/bash

cd /home/destiny/Obsidian/Destiny/Three_Brain_Architecture || exit 1

source /home/destiny/Obsidian/Destiny/Three_Brain_Architecture/voice_env/bin/activate

exec python /home/destiny/Obsidian/Destiny/Three_Brain_Architecture/destiny_jarvis.py
