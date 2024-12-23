from pixels import pixels
from tools import get_color, prompt_color
import random
import asyncio
from InquirerPy import inquirer

async def draw():
    y = 0
    for y in range(7):
        values = await inquirer.text(f"{y}:").execute_async()
        for x in range(6):
            try:
                v = values[x]
            except IndexError:
                v = 0
            pixels.set(x, y, get_color(v))
        pixels.show()

def fill():
    y = 0
    for y in range(7):
        for x in range(6):
            pixels.set(x, y, pixels.default_color)
    pixels.show()

def rand():
    for y in range(7):
        for x in range(6):
            color = get_color(random.choice("rgbwmyco0"))
            pixels.set(x, y, color)
    pixels.show()

async def animate():
    stop_event = asyncio.Event()

    async def go():
        while not stop_event.is_set():
            rand()
            await asyncio.sleep(0.2)

    async def stop():
        await inquirer.text(message="Quitter:").execute_async()
        stop_event.set()

    await asyncio.gather(go(), stop())