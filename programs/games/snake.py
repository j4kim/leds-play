from driver import driver
from .base import BaseGame
import asyncio

class Snake(BaseGame):
    def __init__(self):
        super().__init__()
        self.dir = (0, -1)
        self.nextdir = (0, -1)
        self.head = (0, 7)
        self.body = [(0, 7)] * 10
        self.fps = 3
        self.game_is_over = False

    def frame(self):
        if not self.game_is_over:
            self.move()
            self.draw()

    async def game_over(self):
        self.game_is_over = True
        driver.fill(color = 0xff0000)
        await asyncio.sleep(1/self.fps)
        self.draw()

    def move(self):
        self.dir = self.nextdir
        hx, hy = self.head
        nx = hx + self.dir[0]
        ny = hy + self.dir[1]
        if not self.inscreen(nx, ny):
            asyncio.create_task(self.game_over())
        else:
            self.head = (nx, ny)
            self.body.insert(0, (hx, hy))
            self.body.pop()

    def draw(self):
        driver.clear(False)
        x, y = self.head
        driver.set(x, y, 0x00ff00)
        for x, y in self.body:
            if self.inscreen(x, y):
                driver.set(x, y, 0x00cc00)
        driver.show()

    def change_dir(self, x, y):
        if self.dir[0] != x and self.dir[1] != y:
            self.nextdir = (x, y)

    def on_arrow_up(self): self.change_dir(0, -1)
    def on_arrow_down(self): self.change_dir(0, 1)
    def on_arrow_left(self): self.change_dir(-1, 0)
    def on_arrow_right(self): self.change_dir(1, 0)

    def inscreen(self, x, y):
        return 0 <= x <= 5 and 0 <= y <= 6
