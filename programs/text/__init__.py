from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pixels import pixels
import time
import os.path

def generate_bitmap(text, padding = 6, size=8):
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "PressStart2P-Regular.ttf"), size)
    w = len(text) * size + padding * 2
    image = Image.new("1", (w, size), 0)
    draw = ImageDraw.Draw(image)
    draw.text((padding, 0), text, font=font, fill=1)
    return np.array_split(list(image.getdata()), size)

def frame(values, offset = 0):
    for y in range(7):
        for x in range(6):
            color = pixels.default_color if values[y][x + offset] == 1 else 0
            pixels.set(x, y, color)
    pixels.show()

def scroll(values, offset = 0, fps = 10):
    try:
        frame(values, offset)
        time.sleep(1/fps)
        scroll(values, offset + 1, fps)
    except IndexError:
        pass

def text():
    values = generate_bitmap(input("Text: "))
    scroll(values)

def char():
    values = generate_bitmap(input("Char: "), 0)
    frame(values)