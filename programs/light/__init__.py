from collections import deque
from driver import driver, motion_driver
import asyncio
from tools import get_color


class Light:
    def __init__(self):
        self.quit = asyncio.Event()
        self.color = get_color("W")
        self.lines = 0
        self.motion_history = deque([0] * 10, maxlen=10)
        self.update_counter = 0

    @classmethod
    async def run(cls):
        light = cls()
        await motion_driver.initialize()
        await light.loop()
        driver.clear()

    async def loop(self):
        while not self.quit.is_set():
            self.frame()
            await asyncio.sleep(0.5)

    def frame(self):
        motion = motion_driver.read()
        self.motion_history.append(1 if motion else 0)

        self.update_counter += 1
        if self.update_counter % 2 != 0:
            return

        total = sum(self.motion_history)
        delta = 1 if total > 0 else -1
        lines = max(0, min(self.lines + delta, 7))
        if self.lines == lines:
            return
        self.lines = lines

        driver.clear(False)
        for y in range(6, 6 - self.lines, -1):
            for x in range(6):
                driver.set(x, y, self.color)
        driver.show()
