from . import base, snake, quack, paint
import asyncio
from ..text.tools import minscroll
from driver import driver
from InquirerPy.utils import patched_print

class Menu(base.BaseGame):
    def __init__(self):
        super().__init__()
        self.selected = 0
        self.items = [
            {'value': snake.Snake.run, 'name': 'Snake', 'colors': (0x00ff00, 0)},
            {'value': quack.Quack.run, 'name': 'Quack', 'colors': (0x0000ff, 0)},
            {'value': paint.Paint.run, 'name': 'Paint', 'colors': (0xffff00, 0)},
        ]
        self.menu_task = asyncio.create_task(self.show_selected())

    async def show_selected(self):
        selected = self.items[self.selected]
        while True:
            await minscroll(selected['name'], 5, 5, selected['colors'], 1)
            await asyncio.sleep(1)

    def move(self, diff):
        self.selected = (self.selected + diff) % len(self.items)
        self.menu_task.cancel()
        self.menu_task = asyncio.create_task(self.show_selected())

    def on_arrow_up(self):
        self.move(-1)

    def on_arrow_down(self):
        self.move(1)

    async def start_game(self):
        driver.stop_listening_controllers()
        self.menu_task.cancel()
        await self.items[self.selected]['value']()
        self.listen()
        self.menu_task = asyncio.create_task(self.show_selected())
        patched_print("Menu resumed. Press select to quit")

    def on_start(self):
        asyncio.create_task(self.start_game())

    def cleanup(self):
        self.menu_task.cancel()
