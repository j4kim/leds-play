import os


class FileMotionDriver:
    file_path = os.path.join(os.path.dirname(__file__), "motion.txt")

    async def initialize(self):
        pass

    def read(self):
        with open(self.file_path, "r") as f:
            return f.read() == "1"

    def quit(self):
        pass
