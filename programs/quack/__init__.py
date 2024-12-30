import asyncio
import os.path
from ..image import open_image, show_image
from web import ws_server
from driver import driver

async def quack():
    quit = asyncio.Event()

    im = open_image("quack.gif", os.path.dirname(__file__))
    show_image(im)

    async def handle_event(event):
        if event['value'] == 1:
            if event['key'] == 'south':
                im.seek(1)
                show_image(im)
                ws_server.playsound("coin.wav")
                await asyncio.sleep(0.3)
                im.seek(0)
                show_image(im)
            elif event['key'] == 'select':
                quit.set()

    try:
        driver.listen_controllers(handle_event)
    except Exception as e:
        print(e)
        return

    print("Press select to quit")

    await quit.wait()
    driver.clear()
    driver.stop_listening_controllers()