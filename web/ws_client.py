import asyncio
from websockets.asyncio.client import connect


async def send(message):
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send(message)


def play_sound(filename):
    asyncio.create_task(send(f'{{"sound": "{filename}"}}'))
