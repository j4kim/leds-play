import asyncio
from websockets.asyncio.server import serve, broadcast
from InquirerPy.utils import patched_print

queue = asyncio.Queue()

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    patched_print("new webscoket connection, total:", len(CONNECTIONS))
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def wait_for_messages():
    while True:
        message = await queue.get()
        broadcast(CONNECTIONS, message)

async def start():
    asyncio.create_task(wait_for_messages())
    async with serve(register, "0.0.0.0", 8765) as server:
        patched_print("websocket server started on ws://0.0.0.0:8765")
        await server.serve_forever()

async def stop():
    for connection in set(CONNECTIONS):
        await connection.close()

def playsound(name):
    queue.put_nowait(f'{{"action": "play_sound", "sound": "{name}"}}')

def pausesound(name):
    queue.put_nowait(f'{{"action": "pause_sound", "sound": "{name}"}}')

def resumesound(name):
    queue.put_nowait(f'{{"action": "resume_sound", "sound": "{name}"}}')

def setvolume(name, volume):
    queue.put_nowait(f'{{"action": "set_volume", "sound": "{name}", "volume": {volume}}}')

def stopsounds():
    queue.put_nowait(f'{{"action": "stop_sounds"}}')

def fade(name, f, t, d):
    queue.put_nowait(f'{{"action": "fade", "sound": "{name}", "from": {f}, "to": {t}, "duration": {d}}}')