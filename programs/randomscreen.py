from pixels import pixels
import random
from tools import get_color

def run():
    for y in range(7):
        for x in range(6):
            color = get_color(random.choice("rgbwmyco0"))
            pixels.set(x, y, color)
    pixels.handler.show()
