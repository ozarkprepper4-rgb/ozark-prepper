import os
import sys

desktop_path = os.path.expanduser("~/Desktop")
launcher_path = os.path.join(desktop_path, "Destiny.desktop")

desktop_content = """[Desktop Entry]
Type=Application
Name=Destiny
Comment=Top of the line native Destiny interface
Exec=gnome-terminal -- bash -c "cd ~/Obsidian/Destiny/Three_Brain_Architecture && ./destiny; exec bash"
Icon=utilities-terminal
Terminal=true
Categories=Utility;Application;
"""

with open(launcher_path, "w") as f:
    f.write(desktop_content)

os.chmod(launcher_path, 0o755)
print("DESTINY_UI_BUILT_SUCCESS")
