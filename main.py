from pynput import keyboard
from file_manager import LogFile
from handler import KeyboardHandler


def main():
    log = LogFile()
    kb = KeyboardHandler(log)

    print(f"Logging to: {log.filename}  |  Press ESC to stop")

    with keyboard.Listener(on_press=kb.on_press, on_release=kb.on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()