import asyncio
from web import ws_server

class WebDriver:
    cells = ()
    default_color = 0xffffff
    running = True
    on_event = None
    brightness = 1

    def reset(self):
        pass

    def __init__(self):
        self.clear()

    async def run(self):
        while self.running:
            await asyncio.sleep(1/60)

    def listen_controllers(self, on_event):
        # No input for web driver
        pass

    def stop_listening_controllers(self):
        pass

    def quit(self):
        self.running = False

    def fill(self, *args):
        self.fillscreen(*args)

    def fillscreen(self, show=True, color=None):
        for y in range(7):
            for x in range(6):
                self.cells[y][x] = color or self.default_color
        if show: self.show()

    def clear(self, show=True):
        self.cells = (
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        )
        if show: self.show()

    def set(self, x, y, color):
        self.cells[y][x] = color

    def show(self):
        # Send the entire grid to the web client
        ws_server.update_grid(self.cells)