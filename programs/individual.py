import neopixel
from InquirerPy import inquirer
from config import config

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=config['n'],
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    pixels = neopixel.NeoPixel(**config)

    color = [0, 0, 0]
    for i in range(3):
        name = ["red", "green", "blue"][i]
        max = 9
        color[i] = inquirer.number(
            message=f"value for {name} (0-{max}):",
            min_allowed=0,
            max_allowed=max,
            filter= lambda x: int(int(x) * (255/max))
        ).execute()

    pixels[index] = color
    pixels.show()
