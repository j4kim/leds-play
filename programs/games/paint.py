from driver import driver
from .base import BaseGame
from InquirerPy.utils import patched_print

class Paint(BaseGame):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.state = (
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        )
        self.blinker = self.get_blinker_generator()
        self.color = (255, 255, 255)
        self.black_white = self.get_black_white_generator()

    def frame(self):
        for y in range(7):
            for x in range(6):
                driver.set(x, y, self.state[y][x])
        color = next(self.blinker)
        if color is not None:
            driver.set(self.x, self.y, color)
        driver.show()

    def move(self, x, y):
        self.x = (self.x + x) % 6
        self.y = (self.y + y) % 7

    def get_blinker_generator(self):
        repeat = self.fps // 3
        while True:
            for color in [0x505050, self.color, 0x505050, None]:
                for _ in range(repeat):
                    yield color

    def apply(self):
        self.state[self.y][self.x] = self.color

    def get_black_white_generator(self):
        while True:
            yield (0, 0, 0)
            yield (255, 255, 255)

    def on_arrow_up(self): self.move(0, -1)
    def on_arrow_down(self): self.move(0, 1)
    def on_arrow_left(self): self.move(-1, 0)
    def on_arrow_right(self): self.move(1, 0)
    def on_south(self): self.apply()
    def on_east(self): self.color = next(self.black_white)