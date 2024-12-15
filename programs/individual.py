from InquirerPy import inquirer
from pixels import pixels
from programs.tools import prompt_color

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=pixels.n - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    pixels.handler[index] = prompt_color()
