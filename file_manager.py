import os


def get_filename() -> str:
    if not os.path.exists("txt.txt"):
        return "txt.txt"
    i = 1
    while os.path.exists(f"txt{i}.txt"):
        i += 1
    return f"txt{i}.txt"


class LogFile:
    def __init__(self):
        self.filename = get_filename()
        self._file = open(self.filename, "a", encoding="utf-8", buffering=1)

    def write(self, text: str):
        self._file.write(text)
        self._file.flush()

    def close(self):
        self._file.close()