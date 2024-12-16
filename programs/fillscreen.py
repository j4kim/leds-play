from pixels import pixels
from tools import prompt_color

def run():
    color = prompt_color()
    y = 0
    for y in range(7):
        for x in range(6):
            pixels.set(x, y, color)
