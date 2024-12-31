from driver import driver
import asyncio

class Snake:
    def __init__(self):
        self.dir = (0, -1)
        self.head = (0, 6)
        self.quit = asyncio.Event()
        self.fps = 3

    def handle_event(self, event):
        if event['value'] != 1:
            return
        if event['key'] == 'arrow_up':
            self.dir = (0, -1)
        elif event['key'] == 'arrow_down':
            self.dir = (0, 1)
        elif event['key'] == 'arrow_left':
            self.dir = (-1, 0)
        elif event['key'] == 'arrow_right':
            self.dir = (1, 0)
        elif event['key'] == 'select':
            self.quit.set()

    def draw(self):
        driver.clear()
        x, y = self.head
        driver.set(x, y, 0x00ff00)

    def move(self):
        x = max(0, min(5, self.head[0] + self.dir[0]))
        y = max(0, min(6, self.head[1] + self.dir[1]))
        self.head = (x, y)

    async def run(self):
        while not self.quit.is_set():
            self.draw()
            self.move()
            driver.show()
            await asyncio.sleep(1/self.fps)

async def run():
    snake = Snake()

    try:
        driver.listen_controllers(snake.handle_event)
    except Exception as e:
        print(e)
        return

    print("Press select to quit")

    await snake.run()

    driver.clear()
    driver.stop_listening_controllers()
