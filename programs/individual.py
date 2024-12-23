from InquirerPy import inquirer
from pixels import pixels
from tools import prompt_color

async def run():
    index = await inquirer.number(
        message="Pixel index:",
        max_allowed=pixels.n - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute_async()

    pixels.handler[index] = await prompt_color()
    pixels.handler.show()
