import board
import neopixel
from matrix import matrix

class Pixels:
    handler = None
    pin = board.D18
    n = 300
    brightness = 0.1
    default_color = 0xffffff

    def reset(self):
        self.handler = neopixel.NeoPixel(
            self.pin,
            self.n,
            brightness=self.brightness,
            auto_write=False
        )

    def __init__(self):
        self.reset()

    def fill(self):
        self.handler.fill(self.default_color)
        self.handler.show()

    def clear(self):
        self.handler.fill(0)
        self.handler.show()

    def set(self, x, y, color):
        i = matrix[y][x]
        self.handler[i] = color

pixels = Pixels()