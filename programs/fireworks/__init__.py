import os.path
from ..image import open_image, gif
import asyncio

async def run():
    images = [open_image(f"{i}.gif", os.path.dirname(__file__)) for i in range(10)]

    wait = [1, 0.5, 0.5, 2, 1, 0.2, 0.2, 0.2, 2, 0]

    for i, image in enumerate(images):
        await gif(image, 4)
        await asyncio.sleep(wait[i])