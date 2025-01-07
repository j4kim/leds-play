from . import base, snake, quack, paint
import asyncio
from ..text.tools import minscroll

class Menu(base.BaseGame):
    def __init__(self):
        super().__init__()
        self.selected = 0
        self.items = [
            {'value': snake.Snake.run, 'name': 'Snake'},
            {'value': quack.Quack.run, 'name': 'Quack'},
            {'value': paint.Paint.run, 'name': 'Paint'},
        ]
        self.menu_task = asyncio.create_task(self.show_selected())

    async def show_selected(self):
        selected = self.items[self.selected]
        while True:
            await minscroll(selected['name'], 5, 5, padding=1)
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
        self.quit.set()
        await self.done.wait()
        self.menu_task.cancel()
        await self.items[self.selected]['value']()
        await self.run()

    def on_start(self):
        asyncio.create_task(self.start_game())

    def cleanup(self):
        self.menu_task.cancel()
