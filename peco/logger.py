from datetime import datetime


class Logger:
    def __init__(self, filepath, enabled=True):
        self.filepath = filepath
        self.enabled = enabled

    def log(self, text, end="\n"):
        if not self.enabled:
            return

        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open(self.filepath, "w") as f:
            f.write(f"[{now}]: {text}{end}")
