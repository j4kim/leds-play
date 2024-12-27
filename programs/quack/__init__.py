import asyncio
import os.path
from ..image import open_image, show_image
import pygame

async def quack():
    im = open_image("quack.gif", os.path.dirname(__file__))
    pygame.mixer.init()
    sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "coin.wav"))
    show_image(im)
    await asyncio.sleep(0.5)
    im.seek(1)
    show_image(im)
    sound.play()
    await asyncio.sleep(0.3)
    im.seek(0)
    show_image(im)
    await asyncio.sleep(0.5)
    im.close()