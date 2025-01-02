from driver import driver
from .base import BaseGame

class Snake(BaseGame):
    dir = (0, -1)
    nextdir = (0, -1)
    head = (0, 7)
    body = [(0, 7)] * 10

    def frame(self):
        self.move()
        self.draw()

    def on_arrow_up(self):
        if self.dir[0] != 0:
            self.nextdir = (0, -1)

    def on_arrow_down(self):
        if self.dir[0] != 0:
            self.nextdir = (0, 1)

    def on_arrow_left(self):
        if self.dir[1] != 0:
            self.nextdir = (-1, 0)

    def on_arrow_right(self):
        if self.dir[1] != 0:
            self.nextdir = (1, 0)

    def inscreen(self, x, y):
        return 0 <= x <= 5 and 0 <= y <= 6

    def draw(self):
        driver.clear(False)
        x, y = self.head
        driver.set(x, y, 0x00ff00)
        for x, y in self.body:
            if self.inscreen(x, y):
                driver.set(x, y, 0x00cc00)
        driver.show()

    def move(self):
        self.dir = self.nextdir
        hx, hy = self.head
        nx = hx + self.dir[0]
        ny = hy + self.dir[1]
        if self.inscreen(nx, ny):
            self.head = (nx, ny)
            self.body.insert(0, (hx, hy))
            self.body.pop()
