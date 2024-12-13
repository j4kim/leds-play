from InquirerPy import inquirer
from pixels import config, pixels

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=config['n'] - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    pixels[index] = inquirer.text(
        message=f"hex value:",
        filter= lambda x: int(x, 16)
    ).execute()
