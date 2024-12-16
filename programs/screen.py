from pixels import pixels
from tools import get_color, prompt_color
import random
import time

def draw():
    y = 0
    for y in range(7):
        values = input(f"{y}: ").split()
        for x in range(6):
            try:
                v = values[x]
            except IndexError:
                v = 0
            pixels.set(x, y, get_color(v))
        pixels.handler.show()

def fill():
    color = prompt_color()
    y = 0
    for y in range(7):
        for x in range(6):
            pixels.set(x, y, color)
    pixels.handler.show()

def rand():
    for y in range(7):
        for x in range(6):
            color = get_color(random.choice("rgbwmyco0"))
            pixels.set(x, y, color)
    pixels.handler.show()

def animate():
    try:
        while True:
            rand()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
