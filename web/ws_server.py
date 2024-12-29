import asyncio
from websockets.asyncio.server import serve, broadcast
from InquirerPy.utils import patched_print

serving = asyncio.Event()

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    async for message in websocket:
        broadcast(CONNECTIONS, message)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def start():
    async with serve(register, "localhost", 8765) as server:
        patched_print("websocket server started on ws://localhost:8765")
        serving.set()
        await server.serve_forever()

async def stop():
    for connection in set(CONNECTIONS):
        await connection.close()