import os.path
from ..image import open_image, gif
import asyncio
from web import ws_server
from InquirerPy import inquirer

images = [open_image(f"gifs/{i}.gif", os.path.dirname(__file__)) for i in range(10)]

async def individual():
    index = 0
    while True:
        index = await inquirer.number(
            message="Index or -1 to quit:",
            max_allowed=len(images) - 1,
            min_allowed=-1,
            filter=lambda x: int(x),
            default=index
        ).execute_async()
        if index == -1:
            return
        await gif(images[index], 3)

async def run():
    wait = [1, 0.5, 0.5, 2, 1, 0.2, 0.2, 0.2, 2, 0]

    for i, image in enumerate(images):
        ws_server.queue.put_nowait(f"firework-{i}")
        await gif(image, 3)
        await asyncio.sleep(wait[i])