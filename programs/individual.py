import neopixel
from InquirerPy import inquirer
from config import config

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=config['n'] - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    pixels = neopixel.NeoPixel(**config)

    pixels[index] = inquirer.text(
        message=f"hex value:",
        filter= lambda x: int(x, 16)
    ).execute()

    pixels.show()
