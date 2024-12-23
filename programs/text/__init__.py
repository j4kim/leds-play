from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pixels import pixels
import time
import os.path
import urllib.request
import json

fonts = [
    {
        "file": "PressStart2P-Regular.ttf",
        "size": 8,
        "origin": (0, 0),
    },
    {
        "file": "A Goblin Appears!.otf",
        "size": 7,
        "origin": (0, 0),
    },
    {
        "file": "Pixeled.ttf",
        "size": 5,
        "origin": (0, -4),
    },
    {
        "file": "04B_03__.TTF",
        "size": 8,
        "origin": (0, -1),
    },
    {
        "file": "CWEBS.TTF",
        "size": 13,
        "origin": (0, -6),
    },
    {
        "file": "Rove's-SmolPixelz-4.ttf",
        "size": 4,
        "origin": (0, 7),
    },
]

default_font_index = 1

default_fps = 8

def generate_bitmap(text, font_index = None):
    font = fonts[font_index or default_font_index]
    path = os.path.join(os.path.dirname(__file__), font["file"])
    image_font = ImageFont.truetype(path, font["size"])
    w = len(text) * 8
    image = Image.new("1", (w, 7), 0)
    draw = ImageDraw.Draw(image)
    draw.text(font["origin"], text, font=image_font, fill=1)
    return (
        np.array_split(list(image.getdata()), 7),
        draw.textlength(text, image_font)
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

def padscroll(text, fps = None, font_index = None):
    bitmap, width = generate_bitmap(text, font_index)
    offset = -6
    while offset < width:
        frame(bitmap, offset)
        time.sleep(1/(fps or default_fps))
        offset += 1

def padscroll_input():
    padscroll(input("Text: "))

def minscroll(text, fps = None, font_index = None):
    bitmap, width = generate_bitmap(text, font_index)
    offset = 0
    while offset == 0 or offset < width - 6:
        frame(bitmap, offset)
        time.sleep(1/(fps or default_fps))
        offset += 1

def minscroll_input():
    minscroll(input("Text: "))

def char():
    bitmap, width = generate_bitmap(input("Char: "))
    frame(bitmap)

def random_word():
    data = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?lang=fr&length=5").read().decode("utf-8")
    word = json.loads(data)[0]
    padscroll(word)
    print(word)