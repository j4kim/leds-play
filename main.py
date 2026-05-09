import asyncio
import app
from driver import driver
from web import ws_server


async def main():
    ws_server_task = asyncio.create_task(ws_server.start())
    await asyncio.gather(app.run(), driver.run())
    await ws_server.stop()
    ws_server_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
