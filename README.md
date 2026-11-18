# Noita Python Automation 🧙‍♂️💥🧨 *(WIP)*

A lightweight Python script designed to automate input sequences and handle custom macros in *Noita*, bypassing Windows DirectInput restrictions.

## What it does
- Intercepts global keyboard input using `pynput` (works even while playing in full-screen).
- Sends precise action sequences (`pyautogui`) with built-in cooldown logic to prevent spamming.
- Avoids conflicts while moving/flying in-game.

## Requirements
Make sure you have Python installed, then run the dependencies via terminal:

```bash
py -m pip install pynput pyautogui
```

## How to Run

> **Important:** You must run your terminal, command prompt, or code editor as **Administrator** so Windows allows the script to read global inputs while *Noita* is running in the background/fullscreen.

1. Clone or download this repository.
2. Install the required dependencies via terminal:
   ```bash
   py -m pip install pynput pyautogui
   ```
3. Run the script:
   ```bash
   python kick.py
   ```
4. Open *Noita*, press your assigned macro key, and have fun.
