from pathlib import Path
import glob

class Site:
    def __init__(self, source, dest):
        self.source = Path()
        self.dest = Path()

    def create_dir(self, path):
        directory = f"{self.dest}/{self.source.relative_to()}"
        Path(directory).mkdir(parents=True, exist_ok=True)
    def build(self):
        Path(self.dest).mkdir(parents=True, exist_ok=True)
        for i in self.source.rglob("*"):
            if i.is_dir():
                self.create_dir(i)
