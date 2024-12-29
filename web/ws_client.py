import asyncio
from websockets.asyncio.client import connect
from InquirerPy.utils import patched_print

queue = asyncio.Queue()

connected = False


async def connect_to_server():
    global connected
    try:
        async with connect("ws://localhost:8765") as websocket:
            connected = True
            while True:
                message = await queue.get()
                await websocket.send(message)
    except Exception:
        patched_print("Unable to connect to websocket server")
    finally:
        connected = False


def play_sound(filename):
    if connected:
        queue.put_nowait(f'{{"sound": "{filename}"}}')
