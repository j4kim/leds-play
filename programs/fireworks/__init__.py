import os.path
from ..image import open_image, gif
import asyncio
from web import ws_server
from InquirerPy import inquirer

images = [open_image(f"gifs/{i}.gif", os.path.dirname(__file__)) for i in range(10)]

async def fire(index):
    ws_server.queue.put_nowait(f"firework-{index}")
    await gif(images[index], 3)

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
        await fire(index)

async def run():
    wait = [1, 0.5, 0.5, 2, 1, 0.2, 0.2, 0.2, 2, 0]

    for i, s in enumerate(wait):
        await fire(i)
        await asyncio.sleep(s)