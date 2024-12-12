import neopixel
from config import config

def run():
    pixels = neopixel.NeoPixel(**config)
    pixels.deinit()
