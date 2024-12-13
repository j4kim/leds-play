from InquirerPy import inquirer
from pixels import pixels

def run():
    index = inquirer.number(
        message="Pixel index:",
        max_allowed=pixels.n - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute()

    color = inquirer.text(
        message="hex value or one of r,g,b,w,m,y,c:"
    ).execute()

    mapping = {
        'r': 'ff0000',
        'g': '00ff00',
        'b': '0000ff',
        'w': 'ffffff',
        'm': 'ff00ff',
        'y': 'ffff00',
        'c': '00ffff',
    }

    if color in mapping:
        color = mapping[color]

    pixels.handler[index] = int(color, 16)
