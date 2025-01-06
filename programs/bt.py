from InquirerPy import inquirer
from InquirerPy.utils import patched_print
from driver import driver
import asyncio

async def testControllers():
    def handle_event(event):
        patched_print(event)

    try:
        driver.listen_controllers(handle_event)
    except Exception as e:
        patched_print(e)
        return

    await inquirer.text(message="Press Enter to quit").execute_async()
    driver.stop_listening_controllers()

async def freeThePixel():
    quit = asyncio.Event()

    x = 0
    y = 0

    def handle_event(event):
        nonlocal x, y

        if event['value'] == 1:
            driver.set(x, y, 0)
            if event['key'] == 'arrow_up':
                y -= 1
            elif event['key'] == 'arrow_down':
                y += 1
            elif event['key'] == 'arrow_left':
                x -= 1
            elif event['key'] == 'arrow_right':
                x += 1
            elif event['key'] == 'select':
                quit.set()
            x = max(0, min(5, x))
            y = max(0, min(6, y))
            driver.set(x, y, driver.default_color)
            driver.show()

    try:
        driver.listen_controllers(handle_event)
    except Exception as e:
        patched_print(e)
        return

    patched_print("Press select to quit")

    await quit.wait()
    driver.clear()
    driver.stop_listening_controllers()
