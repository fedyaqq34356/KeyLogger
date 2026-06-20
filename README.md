# KeyLogger

A lightweight, cross-platform keylogger written in Python.
Captures keyboard input and saves it to `.txt` files in real time.
Works on **Linux** (any distribution) and **Windows 10/11**.

---

## Features

### Core Functionality

- **Real-time Saving**: Every keystroke is written and flushed to disk instantly
- **Auto File Naming**: Automatically creates numbered files if a log already exists
- **Unicode Support**: Correctly records all languages — Russian, Ukrainian, Chinese, Arabic, etc.
- **Special Key Handling**: Space, Enter, Tab written as real characters; others like `[BS]`, `[DEL]` in brackets
- **Clean Exit**: Press `ESC` to stop the logger gracefully

### File Naming Logic

| Situation | File Created |
|-----------|-------------|
| First run | `txt.txt` |
| `txt.txt` exists | `txt1.txt` |
| `txt.txt` and `txt1.txt` exist | `txt2.txt` |
| And so on... | `txt3.txt`, `txt4.txt`, ... |

---

## Requirements

- Python 3.8+
- `pynput` library

---

## Installation

**Clone the repository:**

```bash
git clone https://github.com/fedyaqq34356/KeyLogger.git
cd keylogger
```

**Create virtual environment:**

```bash
python -m venv venv
```

**Activate virtual environment:**

Windows:
```bash
venv\Scripts\activate
```

Linux / macOS:
```bash
source venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Usage

**Run the keylogger:**

```bash
python main.py
```

On Linux, you may need root privileges:

```bash
sudo /path/to/venv/bin/python main.py
```

**Console output:**

```
[KeyLogger] Saving to: txt.txt
[KeyLogger] Press ESC to stop.
```

**Stop the keylogger:**

Press `ESC` — the file will be saved and closed automatically.

---

## Project Structure

```
keylogger/
├── main.py           # Entry point, keyboard listener
├── logger.py         # File management and write logic
├── config.py         # Configuration (filename, encoding)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## How It Works

```
User presses a key
        ↓
on_press() in main.py
        ↓
    ├─ Regular key (letter, digit, symbol) → write char as-is
    ├─ Space / Enter / Tab                 → write as real whitespace
    ├─ Backspace / Delete                  → write [BS] / [DEL]
    ├─ Shift / Ctrl / Alt                  → skip (write nothing)
    └─ Other special key                   → write [key_name]
        ↓
KeyLogger.write() in logger.py
        ↓
Immediately flushed to txt.txt
```

---

## Key Behavior Reference

| Key | Written as |
|-----|-----------|
| Letters, digits, symbols | As-is (`a`, `1`, `!`) |
| Space | ` ` (space character) |
| Enter | `\n` (new line) |
| Tab | `\t` (tab) |
| Backspace | `[BS]` |
| Delete | `[DEL]` |
| Caps Lock | `[CAPS]` |
| Shift / Ctrl / Alt | *(nothing)* |
| F1–F12, arrows, etc. | `[f1]`, `[up]`, etc. |
| ESC | Stops the program |

---

## Configuration

Edit `config.py` to change file naming or encoding:

```python
BASE_FILENAME = "txt"    # Base name for log files
EXTENSION = ".txt"       # File extension
ENCODING = "utf-8"       # File encoding (supports all languages)
```

---

## Troubleshooting

**Issue: `ModuleNotFoundError: No module named 'pynput'` with sudo**

When using `sudo`, it uses the system Python, not your venv.

Solution — run with the full path to venv Python:
```bash
sudo /path/to/venv/bin/python main.py
```

Or install pynput to system Python:
```bash
sudo pip install pynput --break-system-packages
```

---

**Issue: No keys being captured on Linux**

Some Linux distributions require the user to be in the `input` group or run as root.

```bash
sudo usermod -aG input $USER
# Then log out and back in
```

---

**Issue: Only gibberish in the file for non-Latin layouts**

Make sure `ENCODING = "utf-8"` is set in `config.py`. Open the `.txt` file with a UTF-8 compatible editor.

---

## Dependencies

- [pynput](https://pypi.org/project/pynput/) — Cross-platform keyboard and mouse monitoring

---

## Acknowledgments

- [pynput](https://pypi.org/project/pynput/) for the excellent cross-platform input monitoring library
- The open-source Python community for making tools like this possible

Made with ❤️ for educational purposes

---

## License

This project is licensed under the **GNU General Public License v3.0**.

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc.
Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

See the full license at: https://www.gnu.org/licenses/gpl-3.0.en.html