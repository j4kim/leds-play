import asyncio
from websockets.asyncio.server import serve, broadcast
from InquirerPy.utils import patched_print

queue = asyncio.Queue()

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
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