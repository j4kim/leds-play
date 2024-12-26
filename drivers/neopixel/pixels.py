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
    controllers = []
    listening_tasks = []

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
        if device not in self.controllers:
            self.controllers.append(device)
        print("Controllers:", self.controllers)

    async def listen_controller(self, device, on_event):
        try:
            while True:
                event = await device.async_read_one()
                on_event(event, device)
        except asyncio.CancelledError:
            pass

    def listen_controllers(self, on_event):
        for device in self.controllers:
            task = asyncio.create_task(self.listen_controller(device, on_event))
            self.listening_tasks.append(task)

    def stop_listening_controllers(self):
        for task in self.listening_tasks:
            task.cancel()
        self.listening_tasks = []

    def quit(self):
        self.clear()
        self.running = False

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