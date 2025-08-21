# BBOT - Simple Game Automation Bot

BBOT is a lightweight automation script that uses Python's `pyautogui` and `pynput` libraries to automate certain mechanics in games, such as clicking, pressing keys, and recognizing screen elements via image matching.

## Features

- Detects specified images on your screen and takes automated actions (keyboard, mouse).
- Simulates keypresses and complex mouse movements.
- Includes a keyboard listener for safe exit (press `ESC` to stop the bot).

## Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/)
- [pynput](https://pypi.org/project/pynput/)

Install dependencies with:

```bash
pip install pyautogui pynput