from driver import driver
from .base import BaseGame
from InquirerPy.utils import patched_print
import asyncio
import time

class Paint(BaseGame):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.state = [[(0,0,0)] * 6 for _ in range(7)]
        self.blinker = self.get_blinker_generator()
        self.color = (255, 255, 255)
        self.rgb_index = 0
        self.forced_pointer_color = None
        self.clear_forced_pointer_task = None
        self.presets = [
            (255, 255, 255), # white
            (255, 0, 0),     # red
            (0, 255, 0),     # green
            (0, 0, 255),     # blue
            (255, 255, 0),   # yellow
            (255, 0, 255),   # magenta
            (0, 255, 255),   # cyan
            (255, 100, 0),   # orange
            (100, 255, 0),   # lime
            (0, 255, 100),   # teak
            (0, 100, 255),   # sky
            (100, 0, 255),   # purple
            (255, 0, 100),   # pink
            (0, 0, 0),       # black
            (100, 100, 100), # gray
        ]
        self.preset_index = 0
        self.last_action = time.time()

    def frame(self):
        for y in range(7):
            for x in range(6):
                driver.set(x, y, self.state[y][x])
        if time.time() - self.last_action < 3:
            self.show_pointer()
        driver.show()

    def show_pointer(self):
        if self.forced_pointer_color is not None:
            driver.set(self.x, self.y, self.forced_pointer_color)
        else:
            driver.set(self.x, self.y, next(self.blinker))

    def move(self, x, y):
        self.x = (self.x + x) % 6
        self.y = (self.y + y) % 7

    def get_blinker_generator(self):
        repeat = self.fps // 3
        while True:
            for color in [0x505050, self.color]:
                for _ in range(repeat):
                    yield color

    def apply(self):
        self.state[self.y][self.x] = self.color

    def change_rgb_index(self):
        self.rgb_index = (self.rgb_index + 1) % 3
        pointer = [0,0,0]
        pointer[self.rgb_index] = 255
        self.force_pointer_color(tuple(pointer))

    async def clear_forced_pointer(self):
        await asyncio.sleep(0.5)
        self.forced_pointer_color = None

    def force_pointer_color(self, color):
        if self.clear_forced_pointer_task is not None:
            self.clear_forced_pointer_task.cancel()
        self.forced_pointer_color = color
        self.clear_forced_pointer_task = asyncio.create_task(self.clear_forced_pointer())

    def set_color(self, color):
        self.color = tuple(color)
        patched_print(f"Color: {self.color}")
        self.force_pointer_color(self.color)

    def tune(self, direction):
        rgb = list(self.color)
        curval = rgb[self.rgb_index]
        if curval == 255:
            curval = 256
        newval = curval + direction * 32
        newval = min(255, max(0, newval))
        rgb[self.rgb_index] = newval
        self.set_color(rgb)

    def inverse(self):
        self.set_color(tuple(255 - x for x in self.color))

    def eyedropper(self):
        self.set_color(self.state[self.y][self.x])

    def next_preset(self):
        self.preset_index = (self.preset_index + 1) % len(self.presets)
        color = self.presets[self.preset_index]
        self.set_color(color)

    def on_arrow_up(self): self.move(0, -1)
    def on_arrow_down(self): self.move(0, 1)
    def on_arrow_left(self): self.move(-1, 0)
    def on_arrow_right(self): self.move(1, 0)
    def on_south(self): self.apply()
    def on_east(self): self.eyedropper()
    def on_west(self): self.change_rgb_index()
    def on_left(self): self.tune(-1)
    def on_right(self): self.tune(1)
    def on_north(self): self.inverse()
    def on_start(self): self.next_preset()
    def on_any(self): self.last_action = time.time()