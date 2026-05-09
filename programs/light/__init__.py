from driver import driver
import asyncio
from tools import get_color


class Light:
    def __init__(self):
        self.quit = asyncio.Event()
        self.motion = False
        self.color = get_color("W")
        self.lines = 3

    @classmethod
    async def run(cls):
        light = cls()
        await light.loop()
        driver.clear()

    async def loop(self):
        while not self.quit.is_set():
            self.frame()
            await asyncio.sleep(1 / 2)

    def frame(self):
        driver.clear(False)
        for y in range(6, 6 - self.lines, -1):
            for x in range(6):
                driver.set(x, y, self.color)
        driver.show()
