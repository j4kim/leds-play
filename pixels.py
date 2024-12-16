import board
import neopixel
from tools import get_color
from matrix import get_index

class Pixels:
    handler = None
    pin = board.D18
    n = 300
    brightness = 0.1
    default_color = 0xffffff

    def reset(self):
        self.handler = neopixel.NeoPixel(self.pin, self.n, brightness=self.brightness)

    def __init__(self):
        self.reset()

    def fill(self):
        self.handler.fill(self.default_color)

    def clear(self):
        self.handler.fill(0)

    def set(self, x, y, color):
        i = get_index(x, y)
        self.handler[i] = color

pixels = Pixels()