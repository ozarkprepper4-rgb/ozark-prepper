# Development Environment — System Profile

**Last verified: August 1, 2026**

---

## Hardware

| Component | Spec |
|---|---|
| CPU | Intel Core i7-4790 @ 3.60GHz (8 cores) |
| RAM | 32GB total, ~27GB available |
| Disk | 916GB SSD — 781GB free |
| GPU | NVIDIA Quadro P620 — 2GB VRAM — Driver 580.173.02 |
| OS | Linux Mint (Ubuntu 24.04 base) |

---

## Core Languages & Runtimes

| Tool | Version | Notes |
|---|---|---|
| Python 3 | 3.12.3 | System python at /usr/bin/python3 |
| pip | 26.1.2 | System-level |
| uv | 0.12.1 | Fast Python package manager — /home/destiny/.local/bin/uv |
| Node.js | v22.23.1 | LTS |
| npm | 10.9.8 | |
| Rust / cargo | 1.96.0 | Installed system-wide |
| Git | 2.43.0 | |

---

## AI & Inference

| Tool | Version | Notes |
|---|---|---|
| Ollama | 0.32.4 | Local LLM server on port 11434 |
| Hermes Agent | 0.19.1 | Primary AI interface |
| ffmpeg | 6.1.1 | Video/audio processing |

### Ollama Models Installed
- hermes3:latest (4.7GB) — used by Pepper and Victoria
- llama3.1:latest (4.9GB) — 131K context
- qwen2.5:14b (9.0GB) — 32K context
- gemma3:4b (3.3GB)
- llama3.2:latest (2.0GB)
- mistral:7b (4.4GB)

---

## Development Tools

| Tool | Version | Notes |
|---|---|---|
| PyCharm Community | 2024.3.4 | Installed via Flatpak |
| VirtualBox | 7.0.16 | Virtual machine manager |
| Docker | 29.1.3 | Container runtime — destiny added to docker group |
| Docker Compose | 1.29.2 | |
| tmux | 3.4 | Terminal multiplexer |
| htop | 3.3.0 | System monitor |
| jq | 1.7 | JSON processor |

---

## Python Virtual Environments

| Name | Path | Purpose |
|---|---|---|
| venv | /home/destiny/venv/ | General Hermes/automation work |
| video_env | /home/destiny/video_env/ | Video processing, YouTube transcript API, Google GenAI |
| ebook_env | /home/destiny/ebook_env/ | Ebook generation tools |

### Key Packages (video_env)
- yt-dlp
- youtube-transcript-api 1.2.4
- google-genai / google-generativeai
- fpdf2 2.8.7
- stripe 15.4.0
- pykeepass

---

## Sudo Configuration

Passwordless sudo configured for destiny user at:
`/etc/sudoers.d/destiny-tools`

Covers: apt-get, apt, flatpak, systemctl, modprobe, snap, tee, chmod, chown, mkdir, dpkg, docker, usermod, install, cp, mv, rm

---

## Services Running

| Service | Port | Notes |
|---|---|---|
| HavenOS | 8000 | Local homestead OS dashboard |
| Ollama | 11434 | Local LLM inference server |
| Docker | — | Container runtime, enabled at startup |

---

## Key File Locations

| Item | Path |
|---|---|
| Hermes config | /home/destiny/.hermes/config.yaml |
| Hermes secrets | /home/destiny/.hermes/.env |
| Pepper profile | /home/destiny/.hermes/profiles/pepper/ |
| Victoria profile | /home/destiny/.hermes/profiles/victoria/ |
| Secure vault | /home/destiny/secure_vault.kdbx |
| Vault key | /home/destiny/.hermes/secure_vault_key.txt |
| Scripts | /home/destiny/scripts/ |
| Obsidian vault | /home/destiny/Obsidian/ |
| Ebook dist folder | /home/destiny/Obsidian/Ozark Prepper/dist/ |

---

## Notes & Limitations

- GPU has only 2GB VRAM — not suitable for GPU-accelerated LLM inference. All Ollama models run on CPU/RAM.
- i7-4790 is a 2014 CPU — capable but will be bottleneck for very large models. Best models for this hardware: 7B-14B parameter range.
- 32GB RAM is the real strength of this machine — allows large models and multiple agents running simultaneously.
- When hardware is upgraded, priority upgrades: GPU with 8GB+ VRAM (enables GPU inference), faster CPU (i9/Ryzen 9).

---

*Linked: [[Destiny]] | [[System Hardware]] | [[HavenOS]]*


## Web learn 2026-09-07 13:33
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-09 01:40
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-09 09:56
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-09 20:24
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-10 04:02
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-10 11:45
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-10 19:21
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-11 03:17
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-11 10:58
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-11 18:39
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-12 02:52
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-12 10:54
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-12 19:22
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-15 21:35
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-15 23:30
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 01:26
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 03:20
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 05:15
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 07:12
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-16 09:06
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 11:01
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-16 12:57
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 14:52
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 16:46
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 18:43
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 20:35
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-16 22:30
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-17 00:26
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-17 02:21
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-17 04:16
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-17 06:12
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-17 08:07
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-17 10:01
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'VisualVM', 'snippet': 'submitting bug reports. Display local and remote Java applications. Display application configuration and runtime environment. Monitor application memory'}]


## Web learn 2026-09-17 11:58
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-17 13:52
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Veolia', 'snippet': 'activities related to sustainable development, professional continuous development and the protection of the environment in France and overseas. The foundation'}]


## Web learn 2026-09-17 15:47
[{'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}, {'title': 'Kiwix', 'snippet': 'and open-source offline web browser created by Emmanuel Engelhart and Renaud Gaudin in 2007. It was first launched to enable offline access to Wikipedia'}]


## Web learn 2026-09-17 17:43
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-17 19:40
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-17 21:37
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 00:13
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 02:10
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 04:06
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 06:03
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 08:00
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 09:58
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 11:55
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 13:51
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 15:48
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 17:45
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 19:43
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 21:39
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-18 23:36
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 01:33
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 03:30
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 05:28
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 07:24
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 09:21
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 11:17
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 13:15
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 15:12
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 17:09
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 19:06
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 21:02
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-19 23:00
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 00:57
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 02:54
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 04:50
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 06:47
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 08:45
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 10:42
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 12:55
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 15:07
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 17:20
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 19:33
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 21:45
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-20 23:58
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-21 02:11
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-21 04:23
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-21 06:36
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-21 11:01
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]


## Web learn 2026-09-21 13:13
[{'title': 'Proxmox Virtual Environment', 'snippet': 'without a separate subscription key. Proxmox Offline Mirror is a command-line tool for maintaining a local APT mirror of Proxmox and Debian repositories'}, {'title': 'Sustainable Development Goals', 'snippet': 'Sustainable Development Goals Wikipedia&#039;s health care articles can be viewed offline with the Medical Wikipedia app. UN Sustainable Development Knowledge'}]
