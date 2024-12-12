import neopixel
from config import config

def run():
    pixels = neopixel.NeoPixel(**config)
    pixels.fill((255, 255, 255))
    pixels.show()
