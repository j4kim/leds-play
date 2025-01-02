import asyncio
import os.path
from programs.image import open_image, show_image
from web import ws_server
from ..base import BaseGame

class Quack(BaseGame):
    def __init__(self):
        super().__init__()
        self.im = open_image("quack.gif", os.path.dirname(__file__))
        self.show_frame(0)
        self.quack_task = None

    def show_frame(self, index):
        self.im.seek(index)
        show_image(self.im)

    def frame(self):
        pass

    async def quack(self):
        self.show_frame(1)
        ws_server.resumesound("coin.wav")
        await asyncio.sleep(0.3)
        self.show_frame(0)

    def on_south(self):
        if self.quack_task:
            self.show_frame(0)
            self.quack_task.cancel()
        self.quack_task = asyncio.create_task(self.quack())
