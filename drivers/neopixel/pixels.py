import board
import neopixel
from .matrix import matrix
import asyncio
from . import bt
import evdev

class Pixels:
    handler = None
    pin = board.D18
    n = 300
    brightness = 0.1
    default_color = 0xffffff
    running = True
    controller_task = None

    def reset(self):
        self.handler = neopixel.NeoPixel(
            self.pin,
            self.n,
            brightness=self.brightness,
            auto_write=False
        )

    def __init__(self):
        self.reset()

    async def run(self):
        pass

    def list_devices(self):
        return bt.list_devices()

    def get_device_name(self, device: evdev.InputDevice):
        return f"{device.name} - {device.path}"

    def add_controller(self, device):
        if self.controller_task is not None: self.controller_task.cancel()
        self.controller_task = asyncio.create_task(bt.listen(device))

    def quit(self):
        self.clear()
        self.running = False
        if self.controller_task is not None: self.controller_task.cancel()

    def fill(self):
        self.handler.fill(self.default_color)
        self.handler.show()

    def clear(self):
        self.handler.fill(0)
        self.handler.show()

    def show(self):
        self.handler.show()

    def set(self, x, y, color):
        i = matrix[y][x]
        self.handler[i] = color