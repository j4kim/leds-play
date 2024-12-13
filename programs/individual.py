from InquirerPy import inquirer
from pixels import pixels

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=pixels.n - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    pixels.handler[index] = inquirer.text(
        message=f"hex value:",
        filter= lambda x: int(x, 16)
    ).execute()
