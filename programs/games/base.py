from driver import driver
import asyncio
from InquirerPy.utils import patched_print
from abc import ABC

class BaseGame(ABC):
    def __init__(self):
        self.quit = asyncio.Event()
        self.fps = 10

    @classmethod
    async def run(cls):
        game = cls()
        try:
            driver.listen_controllers(game.handle_event)
        except Exception as e:
            print(e)
            return
        patched_print("Press select to quit")
        await game.loop()
        driver.clear()
        driver.stop_listening_controllers()

    async def loop(self):
        while not self.quit.is_set():
            self.frame()
            await asyncio.sleep(1/self.fps)

    def frame(self):
        pass

    def handle_event(self, event):
        if event['value'] != 1:
            return
        key = event['key']
        if key == 'select':
            self.quit.set()
            return
        methodname = f'on_{key}'
        method = getattr(self, methodname, None)
        if method:
            method()
        else:
            print(f"Method {methodname} not defined in {self.__class__.__name__}")
