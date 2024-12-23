from InquirerPy import inquirer

def get_color(color):
    mapping = {
        'r': 'ff0000',
        'g': '00ff00',
        'b': '0000ff',
        'w': 'ffffff',
        'm': 'ff00ff',
        'y': 'ffff00',
        'c': '00ffff',
        'o': 'ff5500',
        ' ': 0,
    }

    if color in mapping:
        color = mapping[color]

    return int(str(color), 16)

async def prompt_color(message = "hex value or one of r,g,b,w,m,y,c,o:"):
    color = await inquirer.text(message).execute_async()
    return get_color(color)