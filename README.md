# InstalingBot

InstalingBot is a simple automation tool that interacts with the [Instaling](https://instaling.pl/) platform. It uses Selenium to drive a web browser and a Tkinter-based UI to make it easier to run. Image handling (e.g., icons, screenshots) is supported via Pillow.

Use this project responsibly and only in accordance with Instaling’s Terms of Service. You are solely responsible for how you use this software.

## Features

- Automates routine interactions with Instaling using Selenium
- Cross-platform: Windows, macOS, and Linux (Python 3.x)
- Lightweight UI built with Tkinter
- Simple build process for a standalone executable via PyInstaller

## Prerequisites

- Python 3.x (recommended 3.8+)
- pip
- A supported web browser (Chrome or Firefox recommended)
- Internet connection

Python packages:
- Pillow
- tkinter (bundled with most Python installers; see install guide for OS-specific packages)
- selenium

## Installation

See the full, step-by-step [Installation and Setup Guide](./INSTALL.md).

Quick start:
```bash
# Clone the repository
git clone https://github.com/dzik77/InstalingBot.git
cd InstalingBot

# (Recommended) create and activate a virtual environment, then install deps
python3 -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
python3 -m pip install --upgrade pip
python3 -m pip install Pillow selenium

# On Linux, install Tkinter if missing (examples)
# Debian/Ubuntu: sudo apt install -y python3-tk
# Fedora:        sudo dnf install -y python3-tkinter
# Arch:          sudo pacman -S --needed tk
```

Selenium drivers:
- With Selenium 4.6+, Selenium Manager can automatically fetch the right driver for your installed browser at runtime.
- If you prefer manual setup, download the appropriate driver (e.g., ChromeDriver or GeckoDriver) and ensure it is on your PATH.

## Usage

Run from source:
```bash
# Linux/macOS
python3 main.py

# Windows (PowerShell)
py -3 .\main.py
```

Notes:
- Keep your browser installed and up to date (Chrome or Firefox).
- The UI may prompt you for any necessary inputs at runtime.

## Build (optional)

You can build a standalone executable with the provided PyInstaller spec:
```bash
# Install PyInstaller if needed
python3 -m pip install pyinstaller  # Windows: py -3 -m pip install pyinstaller

# Build using the spec file
pyinstaller main.spec               # Windows: py -3 -m PyInstaller .\main.spec
```

The build artifacts will be placed in the `dist/` directory.

## Troubleshooting

Common issues:
- ModuleNotFoundError: No module named 'tkinter' → Install the OS package (e.g., `python3-tk` on Debian/Ubuntu) or use the official Python installer for your OS.
- Selenium driver/browser errors → Ensure Chrome/Firefox is installed; use Selenium 4.6+ to let Selenium Manager handle drivers automatically.

See more tips in [INSTALL.md](./INSTALL.md).

## Contributing

Issues and pull requests are welcome. Please open an [issue](https://github.com/dzik77/InstalingBot/issues) to report bugs or suggest improvements.

## License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## Disclaimer

- This project is not affiliated with, endorsed, or sponsored by Instaling.
- Use only in accordance with Instaling’s Terms of Service and applicable laws.
- You assume all responsibility for using this software.
