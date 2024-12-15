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

    def set(self, x, y, v):
        i = get_index(x, y)
        color = get_color(v)
        self.handler[i] = color

pixels = Pixels()