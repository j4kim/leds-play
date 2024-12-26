from InquirerPy import inquirer
from pixels import pixels
import asyncio

async def testControllers():
    def handle_event(event):
        print(event)

    try:
        pixels.listen_controllers(handle_event)
    except Exception as e:
        print(e)
        return

    await inquirer.text(message="Press Enter to quit\n").execute_async()
    pixels.stop_listening_controllers()

async def freeThePixel():
    quit = asyncio.Event()

    x = 0
    y = 0

    def handle_event(event):
        nonlocal x, y
        if event['value'] == 2 and event['binding'] == 'select':
            quit.set()

        if event['value'] == 1:
            pixels.set(x, y, 0)
            if event['binding'] == 'arrow_up':
                y -= 1
            elif event['binding'] == 'arrow_down':
                y += 1
            elif event['binding'] == 'arrow_left':
                x -= 1
            elif event['binding'] == 'arrow_right':
                x += 1
            x = max(0, min(5, x))
            y = max(0, min(6, y))
            pixels.set(x, y, pixels.default_color)
            pixels.show()

    try:
        pixels.listen_controllers(handle_event)
    except Exception as e:
        print(e)
        return

    print("Long press select to quit")

    await quit.wait()
    pixels.clear()
    pixels.stop_listening_controllers()
