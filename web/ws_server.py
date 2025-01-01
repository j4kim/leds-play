import asyncio
from websockets.asyncio.server import serve, broadcast
from InquirerPy.utils import patched_print
import json

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

def send(command):
    queue.put_nowait(json.dumps(command))

def playsound(name):
    send({'action': 'play_sound', 'sound': name})

def pausesound(name):
    send({'action': 'pause_sound', 'sound': name})

def resumesound(name):
    send({'action': 'resume_sound', 'sound': name})

def setvolume(name, volume):
    send({'action': 'set_volume', 'sound': name, 'volume': volume})

def stopsounds():
    send({'action': 'stop_sounds'})

def fade(name, f, t, d):
    send({'action': 'fade', 'sound': name, 'from': f, 'to': t, 'duration': d})