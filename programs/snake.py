from driver import driver
import asyncio
from InquirerPy.utils import patched_print

class Snake:
    dir = (0, -1)
    nextdir = (0, -1)
    head = (0, 7)
    body = [(0, 7)] * 10
    quit = asyncio.Event()
    fps = 3

    @classmethod
    async def run(cls):
        snake = cls()
        try:
            driver.listen_controllers(snake.handle_event)
        except Exception as e:
            print(e)
            return
        patched_print("Press select to quit")
        await snake.loop()
        driver.clear()
        driver.stop_listening_controllers()

    async def loop(self):
        while not self.quit.is_set():
            self.move()
            self.draw()
            await asyncio.sleep(1/self.fps)

    def handle_event(self, event):
        if event['value'] != 1:
            return
        if event['key'] == 'arrow_up' and self.dir[0] != 0:
            self.nextdir = (0, -1)
        elif event['key'] == 'arrow_down' and self.dir[0] != 0:
            self.nextdir = (0, 1)
        elif event['key'] == 'arrow_left' and self.dir[1] != 0:
            self.nextdir = (-1, 0)
        elif event['key'] == 'arrow_right' and self.dir[1] != 0:
            self.nextdir = (1, 0)
        elif event['key'] == 'select':
            self.quit.set()

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
