from collections import deque
from driver import driver, motion_driver
import asyncio
from tools import get_color
from InquirerPy import inquirer
from sun import Sun


class Light:
    def __init__(self):
        self.quit = asyncio.Event()
        self.color = get_color("W")
        self.lines = 0
        self.motion_history = deque([0] * 10, maxlen=10)
        self.pir_init_task = None
        self.sun = Sun()

    @classmethod
    async def run(cls):
        light = cls()
        light.start()

    async def start(self):
        self.pir_init_task = asyncio.create_task(motion_driver.initialize())
        self.sun_request_task = asyncio.create_task(self.sun.request())
        await asyncio.gather(self.loop(), self.stop())
        driver.clear()

    async def loop(self):
        while not self.quit.is_set():
            if self.sun.isNight():
                if motion_driver.initialized:
                    self.frame()
                await asyncio.sleep(0.5)
            else:
                driver.clear()
                await asyncio.sleep(60)

    async def stop(self):
        await inquirer.text(message="Quitter:").execute_async()
        if self.pir_init_task:
            self.pir_init_task.cancel()
        if self.sun_request_task:
            self.sun_request_task.cancel()
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
