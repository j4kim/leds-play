from driver import driver
import asyncio
from InquirerPy.utils import patched_print
from abc import ABC

class BaseGame(ABC):
    def __init__(self):
        self.quit = asyncio.Event()
        self.done = asyncio.Event()
        self.fps = 10
        self.running = True

    @classmethod
    async def run(cls):
        game = cls()
        try:
            driver.listen_controllers(game.handle_event)
        except Exception as e:
            print(e)
            return
        patched_print(f"{cls.__name__} started. Press select to quit")
        await game.loop()
        driver.clear()
        driver.stop_listening_controllers()
        game.done.set()

    async def loop(self):
        while not self.quit.is_set():
            if self.running:
                self.frame()
            await asyncio.sleep(1/self.fps)

    # these methods can be overridden in subclasses
    def frame(self): pass
    def on_arrow_up(self): pass
    def on_arrow_right(self): pass
    def on_arrow_down(self): pass
    def on_arrow_left(self): pass
    def on_north(self): pass
    def on_east(self): pass
    def on_south(self): pass
    def on_west(self): pass
    def on_left(self): pass
    def on_right(self): pass

    def on_start(self):
        self.running = not self.running

    def on_select(self): 
        self.quit.set()

    def handle_event(self, event):
        if event['value'] != 1:
            return
        key = event['key']
        methodname = f'on_{key}'
        method = getattr(self, methodname, None)
        method()
