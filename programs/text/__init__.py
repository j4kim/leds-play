from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pixels import pixels
import time
import os.path

def generate_bitmap(text):
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "A Goblin Appears!.otf"), 7)
    w = len(text) * 8
    image = Image.new("1", (w, 7), 0)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=1)
    return (
        np.array_split(list(image.getdata()), 7),
        draw.textlength(text, font)
    )

def frame(bitmap, offset = 0):
    for y in range(7):
        row = bitmap[y]
        for x in range(6):
            ox = x + offset
            if ox < 0 or ox >= len(row):
                color = 0
            else:
                color = pixels.default_color if row[ox] == 1 else 0
            pixels.set(x, y, color)
    pixels.show()

def padscroll(fps = 10):
    bitmap, width = generate_bitmap(input("Text: "))
    offset = -6
    while offset < width:
        frame(bitmap, offset)
        time.sleep(1/fps)
        offset += 1

def minscroll(fps = 5):
    bitmap, width = generate_bitmap(input("Text: "))
    offset = 0
    while offset == 0 or offset < width - 6:
        frame(bitmap, offset)
        time.sleep(1/fps)
        offset += 1

def char():
    bitmap, width = generate_bitmap(input("Char: "))
    frame(bitmap)