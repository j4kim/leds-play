from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pixels import pixels
import time

def generate_bitmap(text, font_path="PressStart2P-Regular.ttf", size=8):
    font = ImageFont.truetype(font_path, size)
    w = len(text) * size + 12
    image = Image.new("1", (w, size), 0)
    draw = ImageDraw.Draw(image)
    draw.text((6, 0), text, font=font, fill=1)
    return np.array_split(list(image.getdata()), size)

def scroll(values, offset = 0, fps = 10):
    try:
        for y in range(7):
            for x in range(6):
                color = pixels.default_color if values[y][x + offset] == 1 else 0
                pixels.set(x, y, color)
        pixels.show()
        time.sleep(1/fps)
        scroll(values, offset + 1, fps)
    except IndexError:
        pass

def run():
    values = generate_bitmap("Hello!")
    scroll(values)