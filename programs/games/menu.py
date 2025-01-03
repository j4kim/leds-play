from . import base, snake, quack
import asyncio
from ..text.tools import minscroll

class Menu(base.BaseGame):
    def __init__(self):
        super().__init__()
        self.selected = 0
        self.items = [
            {'value': snake.Snake.run, 'name': 'Snake'},
            {'value': quack.Quack.run, 'name': 'Quack'},
        ]
        self.menu_task = asyncio.create_task(self.show_selected())

    async def show_selected(self):
        selected = self.items[self.selected]
        await minscroll(selected['name'], 5, 5)

    def move(self, diff):
        self.selected = (self.selected + diff) % len(self.items)
        self.menu_task.cancel()
        self.menu_task = asyncio.create_task(self.show_selected())

    def on_arrow_up(self):
        self.move(-1)

    def on_arrow_down(self):
        self.move(1)

    async def start_game(self):
        self.quit.set()
        await self.done.wait()
        await self.items[self.selected]['value']()
        await self.run()

    def on_start(self):
        self.menu_task.cancel()
        asyncio.create_task(self.start_game())
