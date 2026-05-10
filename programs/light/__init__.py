from collections import deque
from driver import driver, motion_driver
import asyncio
from tools import get_color
from InquirerPy import inquirer
from InquirerPy.utils import patched_print


class Light:
    def __init__(self):
        self.quit = asyncio.Event()
        self.color = get_color("W")
        self.lines = 0
        self.motion_history = deque([0] * 10, maxlen=10)
        self.pir_init_task = None

    @classmethod
    async def run(cls):
        light = cls()
        light.pir_init_task = asyncio.create_task(motion_driver.initialize())
        await asyncio.gather(light.loop(), light.stop())
        driver.clear()

    async def loop(self):
        while not self.quit.is_set():
            if motion_driver.initialized:
                self.frame()
            await asyncio.sleep(0.5)

    async def stop(self):
        await inquirer.text(message="Quitter:").execute_async()
        self.pir_init_task.cancel()
        self.quit.set()

    def frame(self):
        motion = motion_driver.read()
        self.motion_history.append(1 if motion else 0)

        total = sum(self.motion_history)
        delta = 1 if total > 0 else -1
        lines = max(0, min(self.lines + delta, 5))
        if self.lines == lines:
            return
        self.lines = lines

        driver.clear(False)
        for y in range(6, 6 - self.lines, -1):
            for x in range(6):
                driver.set(x, y, self.color)
        driver.show()
