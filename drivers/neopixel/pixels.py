import board
import neopixel
from .matrix import matrix
import asyncio
import evdev

key_bindings = {
    46: 'arrow_up',
    33: 'arrow_right',
    32: 'arrow_down',
    18: 'arrow_left',
    35: 'north',
    34: 'east',
    36: 'south',
    23: 'west',
    37: 'left',
    50: 'right',
    49: 'select',
    24: 'start',
}

class Pixels:
    handler = None
    pin = board.D18
    n = 300
    brightness = 0.1
    default_color = 0xffffff
    running = True
    listening_tasks = []
    devices = []

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

    async def listen_controller(self, path, on_event):
        device = evdev.InputDevice(path)
        self.devices.append(device)
        while True:
            event = await device.async_read_one()
            if event.type == evdev.ecodes.EV_KEY:
                on_event({
                    'value': event.value,
                    'device': path,
                    'key': key_bindings.get(event.code, event.code)
                })

    def listen_controllers(self, on_event):
        device_paths = [
            path for path in evdev.list_devices()
            if path not in ['/dev/input/event0', '/dev/input/event1'] # remove hdmi devices
        ]
        if (len(device_paths) == 0):
            raise Exception("No devices found")
        for path in device_paths:
            task = asyncio.create_task(self.listen_controller(path, on_event))
            self.listening_tasks.append(task)

    def stop_listening_controllers(self):
        for device in self.devices:
            device.close()

        for task in self.listening_tasks:
            task.cancel()

        self.listening_tasks = []
        self.devices = []

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