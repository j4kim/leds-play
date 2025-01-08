import asyncio
import os.path
from programs.image import open_image, show_image
from web import ws_server
from ..base import BaseGame

class Quack(BaseGame):
    def __init__(self):
        super().__init__()
        self.images = {
            'quack': open_image("quack.gif", os.path.dirname(__file__)),
            'woof': open_image("woof.gif", os.path.dirname(__file__)),
            'roar': open_image("roar.gif", os.path.dirname(__file__)),
            'kri': open_image("kri.gif", os.path.dirname(__file__)),
        }
        self.selected = 'quack'
        self.show_frame(0)
        self.task = None

    def show_frame(self, index):
        im = self.images[self.selected]
        im.seek(index)
        show_image(im)

    async def animate(self):
        self.show_frame(1)
        ws_server.resumesound(self.selected)
        await asyncio.sleep(0.3)
        self.show_frame(0)

    def play(self, selected):
        self.selected = selected
        if self.task:
            self.show_frame(0)
            self.task.cancel()
        self.task = asyncio.create_task(self.animate())

    def on_south(self): self.play('quack')
    def on_west(self): self.play('woof')
    def on_north(self): self.play('roar')
    def on_east(self): self.play('kri')
