import asyncio
import os.path
from ..image import open_image, show_image

async def quack():
    im = open_image("quack.gif", os.path.dirname(__file__))
    try:
        while True:
            show_image(im)
            im.seek(im.tell() + 1)
            await asyncio.sleep(0.2)
    except EOFError:
        pass
    finally:
        im.close()