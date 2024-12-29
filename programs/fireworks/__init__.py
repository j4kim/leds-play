from PIL import Image
import os.path
import numpy as np
from driver import driver
import asyncio
from ..image import open_image, gif

async def run():
    im = open_image("fireworks.gif", os.path.dirname(__file__))
    await gif(im)