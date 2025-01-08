import os.path
from ..image import open_image, gif
from web import ws_server
from InquirerPy import inquirer

images = [open_image(f"gifs/{i}.gif", os.path.dirname(__file__)) for i in range(11)]

async def fire(index):
    ws_server.playsound(f"firework-{index}")
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
