import neopixel
from InquirerPy import inquirer
from config import config

def fill(r=255, g=255, b=255):
    pixels = neopixel.NeoPixel(**config)
    pixels.fill((r, g, b))
    pixels.show()

def deinit():
    pixels = neopixel.NeoPixel(**config)
    pixels.deinit()

def setPixelNumber():
    config['n'] = inquirer.number(
        message="Enter number of pixels:",
        default=config['n'],
        min_allowed=-1,
    ).execute()

def setBrightness():
    b = inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=config['brightness'],
        min_allowed=0,
        max_allowed=1,
    ).execute()
    config['brightness'] = float(b)