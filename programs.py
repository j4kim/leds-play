import neopixel
from config import config

def fill(r=255, g=255, b=255):
    pixels = neopixel.NeoPixel(**config)
    pixels.fill((r, g, b))
    pixels.show()

def deinit():
    pixels = neopixel.NeoPixel(**config)
    pixels.deinit()
