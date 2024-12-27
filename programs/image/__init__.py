from PIL import Image
import os.path
import numpy as np
from driver import driver
import asyncio
from PIL import GifImagePlugin
GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_ALWAYS

def show_image(im):
    bitmap = np.array_split(list(im.getdata()), 7)
    for y in range(7):
        for x in range(6):
            driver.set(x, y, bitmap[y][x][:3])
    driver.show()

def duck():
    path = os.path.join(os.path.dirname(__file__), "duck.png")
    with Image.open(path) as im:
        show_image(im)

async def fireworks():
    path = os.path.join(os.path.dirname(__file__), "fireworks.gif")
    with Image.open(path) as im:
        try:
            while True:
                show_image(im)
                im.seek(im.tell() + 1)
                await asyncio.sleep(0.1)
        except EOFError:
            pass