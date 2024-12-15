import board
import neopixel

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

pixels = Pixels()