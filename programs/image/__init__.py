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

def open_image(path, dir = os.path.dirname(__file__)):
    path = os.path.join(dir, path)
    return Image.open(path)

def duck():
    im = open_image("duck.png")
    show_image(im)
    im.close()

async def fireworks():
    im = open_image("fireworks.gif")
    try:
        while True:
            show_image(im)
            im.seek(im.tell() + 1)
            await asyncio.sleep(0.1)
    except EOFError:
        pass
    finally:
        im.close()