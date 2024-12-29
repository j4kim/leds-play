import asyncio
import os.path
from ..image import open_image, show_image
from web import ws_server

async def quack():
    im = open_image("quack.gif", os.path.dirname(__file__))
    show_image(im)
    await asyncio.sleep(0.5)
    im.seek(1)
    show_image(im)
    ws_server.queue.put_nowait("coin.wav")
    await asyncio.sleep(0.3)
    im.seek(0)
    show_image(im)
    await asyncio.sleep(0.5)
    im.close()