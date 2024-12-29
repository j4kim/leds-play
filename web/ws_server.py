import asyncio
from websockets.asyncio.server import serve, broadcast


CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    async for message in websocket:
        broadcast(CONNECTIONS, message)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def main():
    async with serve(register, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
