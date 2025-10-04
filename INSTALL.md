# InstalingBot — Installation and Setup Guide

This guide walks you through installing dependencies, running the app from source, and (optionally) building a standalone executable.

## Prerequisites

- Operating System: Windows 10/11, macOS, or Linux
- Python: 3.x (recommend 3.8+)
- pip (Python package manager)
- A web browser for Selenium (Chrome or Firefox recommended)
- Internet connection

Optional (for building executables):
- PyInstaller

## 1) Get the source

```bash
# Clone the repository
git clone https://github.com/dzik77/InstalingBot.git
cd InstalingBot
```

## 2) Create and activate a virtual environment (recommended)

- Linux / macOS:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- Windows (PowerShell):
  ```powershell
  py -3 -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

## 3) Install dependencies

The project uses:
- Pillow
- tkinter
- selenium

Install Python packages:
```bash
# Linux/macOS
python3 -m pip install --upgrade pip
python3 -m pip install "Pillow" "selenium"
# Windows (PowerShell)
py -3 -m pip install --upgrade pip
py -3 -m pip install "Pillow" "selenium"
```

Install tkinter (if needed):
- Windows: Tkinter is included with the standard Python installer by default.
- macOS: Tkinter is included with the official Python installer from python.org. If it’s missing, install Python from https://www.python.org/downloads/.
- Debian/Ubuntu:
  ```bash
  sudo apt update
  sudo apt install -y python3-tk
  ```
- Fedora:
  ```bash
  sudo dnf install -y python3-tkinter
  ```
- Arch:
  ```bash
  sudo pacman -S --needed tk
  ```

Note on Selenium drivers:
- With Selenium 4.6+, Selenium Manager can automatically fetch the correct browser driver (ChromeDriver/GeckoDriver) at runtime. Ensure you have a supported browser installed (e.g., Google Chrome or Mozilla Firefox).
- If you prefer manual setup, download the appropriate driver and ensure it’s on your PATH.

## 4) Run from source

From the repository root:
```bash
# Linux/macOS
python3 main.py

# Windows (PowerShell)
py -3 .\main.py
```

## 5) Optional: Build a standalone executable with PyInstaller

This step is optional. Skip if you only need to run from source.

Install PyInstaller (if not already installed):
```bash
# Linux/macOS
python3 -m pip install pyinstaller
# Windows
py -3 -m pip install pyinstaller
```

Build using the provided spec file:
```bash
# Linux/macOS
pyinstaller main.spec
# Windows
py -3 -m PyInstaller .\main.spec
```

After a successful build:
- The output is placed in the `dist/` directory (layout depends on your `main.spec` configuration).
- You can distribute the contents of `dist/` to run without Python installed.

## Troubleshooting

- ModuleNotFoundError: No module named 'tkinter'
  - Linux: Install `python3-tk` (Debian/Ubuntu), `python3-tkinter` (Fedora), or `tk` (Arch).
  - macOS: Install Python from python.org to ensure Tkinter is bundled.
  - Windows: Reinstall Python using the official installer and ensure Tcl/Tk is selected (it’s on by default).

- Selenium driver error (e.g., “NoSuchDriver” or browser not found):
  - Ensure Chrome or Firefox is installed.
  - Use Selenium 4.6+ so Selenium Manager can download drivers automatically, or install the appropriate driver and add it to your PATH.

- On macOS, the built app is “damaged” or blocked:
  - Allow the app in System Settings > Privacy & Security, or right-click > Open the first time.

## Optional: Requirements file

If you prefer to pin dependencies, create a simple `requirements.txt`:
```
Pillow
selenium
```
Then install with:
```bash
# Linux/macOS
python3 -m pip install -r requirements.txt
# Windows
py -3 -m pip install -r requirements.txt
```

---

If you run into setup issues, please share your OS, Python version (`python3 --version`), and any error messages.