import os
import asyncio
from InquirerPy.utils import patched_print


class FileMotionDriver:
    file_path = os.path.join(os.path.dirname(__file__), "motion.txt")
    initialized = False

    async def initialize(self):
        if not self.initialized:
            patched_print("Initialisation fake du capteur PIR...")
            await asyncio.sleep(3)
            patched_print("Capteur initialisé")
            self.initialized = True

    def read(self):
        with open(self.file_path, "r") as f:
            return f.read().startswith("1")

    def quit(self):
        pass
