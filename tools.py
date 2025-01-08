from InquirerPy import inquirer
import asyncio
import config

colors = {
    'w': (255, 255, 255), # white
    'r': (255, 0, 0),     # red
    'g': (0, 255, 0),     # green
    'b': (0, 0, 255),     # blue
    'y': (255, 255, 0),   # yellow
    'm': (255, 0, 255),   # magenta
    'c': (0, 255, 255),   # cyan
    'o': (255, 100, 0),   # orange
    'l': (100, 255, 0),   # lime
    't': (0, 255, 100),   # teak
    's': (0, 100, 255),   # sky
    'p': (100, 0, 255),   # purple
    'k': (255, 0, 100),   # pink
    ' ': (0, 0, 0),       # black
    '#': (100, 100, 100), # gray
}

def get_color(color):
    if color in colors:
        return colors[color]
    return int(str(color), 16)

async def prompt_color(message = "hex value or one of r,g,b,w,m,y,c,o:"):
    color = await inquirer.text(message).execute_async()
    return get_color(color)

async def prompt_menu(choices):
    choices = [p for p in choices if p.get('only-for', config.driver) == config.driver]
    f = None
    while True:
        f = await inquirer.select(
            message="Program:",
            choices=[*choices, {'value': 'exit', 'name': 'Exit'}],
            default=lambda _ : f,
        ).execute_async()
        if f == 'exit':
            return
        r = f()
        if asyncio.iscoroutine(r):
            await r