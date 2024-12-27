from PIL import Image, ImageDraw, ImageFont
import numpy as np
from driver import driver
import asyncio
import os.path
import urllib.request
import json
from InquirerPy import inquirer
from . import config

async def menu():
    f = None
    while True:
        choices = [
            {'value': padscroll_input, 'name': 'Text scroll'},
            {'value': minscroll_input, 'name': 'Text min scroll'},
            {'value': char, 'name': 'Char'},
            {'value': random_word, 'name': 'Random word'},
            {'value': setFont, 'name': 'Set default font'},
            {'value': setTextFps, 'name': 'Set default text fps'},
            {'value': 'exit', 'name': 'Exit'}
        ]
        f = await inquirer.select(
            message="Program:",
            choices=choices,
            default=lambda _ : f,
        ).execute_async()
        if f == 'exit':
            return
        r = f()
        if asyncio.iscoroutine(r):
            await r

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

def frame(bitmap, offset = 0):
    for y in range(7):
        row = bitmap[y]
        for x in range(6):
            ox = x + offset
            if ox < 0 or ox >= len(row):
                color = 0
            else:
                color = driver.default_color if row[ox] == 1 else 0
            driver.set(x, y, color)
    driver.show()

async def padscroll(text, fps = None, font_index = None):
    bitmap, width = generate_bitmap(text, font_index)
    offset = -6
    while offset < width:
        frame(bitmap, offset)
        await asyncio.sleep(1/(fps or config.default_fps))
        offset += 1

async def padscroll_input():
    await padscroll(input("Text: "))

async def minscroll(text, fps = None, font_index = None):
    bitmap, width = generate_bitmap(text, font_index)
    offset = 0
    while offset == 0 or offset < width - 6:
        frame(bitmap, offset)
        await asyncio.sleep(1/(fps or config.default_fps))
        offset += 1

async def minscroll_input():
    await minscroll(input("Text: "))

def char():
    bitmap, width = generate_bitmap(input("Char: "))
    frame(bitmap)

async def random_word():
    data = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?lang=fr&length=5").read().decode("utf-8")
    word = json.loads(data)[0]
    await padscroll(word)
    print(word)

async def setFont():
    config.default_font_index = await inquirer.number(
        message="Default font:",
        min_allowed=0,
        max_allowed=len(config.fonts) - 1,
        filter=lambda x: int(x),
        default=config.default_font_index
    ).execute_async()

async def setTextFps():
    config.default_fps = await inquirer.number(
        message="Defaut text fps:",
        min_allowed=1,
        max_allowed=30,
        filter=lambda x: int(x),
        default=config.default_fps
    ).execute_async()