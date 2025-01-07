from PIL import Image, ImageDraw, ImageFont
import numpy as np
from driver import driver
import asyncio
import os.path
from . import config

def generate_bitmap(text, font_index = None):
    font = config.fonts[font_index or config.default_font_index]
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

def frame(bitmap, offset = 0, colors = None):
    colors = colors or (0xffffff, 0)
    if (callable(colors)):
        colors = colors(offset)
    for y in range(7):
        row = bitmap[y]
        for x in range(6):
            ox = x + offset
            if ox < 0 or ox >= len(row) or row[ox] == 0:
                color = colors[1]
            else:
                color = colors[0]
            driver.set(x, y, color)
    driver.show()

def char(text, font_index = None, colors = None):
    bitmap, width = generate_bitmap(text, font_index)
    frame(bitmap, colors=colors)

async def padscroll(text, fps = None, font_index = None, colors = None):
    await minscroll(text, fps, font_index, colors, padding=6)

async def minscroll(text, fps = None, font_index = None, colors = None, padding = 0):
    bitmap, width = generate_bitmap(text, font_index)
    offset = -padding
    while offset == 0 or offset < width - (6-padding):
        frame(bitmap, offset, colors)
        await asyncio.sleep(1/(fps or config.default_fps))
        offset += 1

def alternate(i, two_color_tuples, multiplier):
    t1 = two_color_tuples[0]
    t2 = two_color_tuples[1]
    return t1 if (i//multiplier) % 2 == 0 else t2

async def funky(fun, text, two_color_tuples, alternator = alternate, bpm = 111, font_index = None, multiplier = 4):
    await fun(text=text, fps=multiplier*(bpm/60), font_index=font_index, colors=lambda i: alternator(i, two_color_tuples, multiplier))