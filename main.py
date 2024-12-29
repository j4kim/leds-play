import asyncio
import prompt
from driver import driver
from web import ws_client
from web import ws_server

async def main():
    ws_server_task = asyncio.create_task(ws_server.start())
    await ws_server.serving.wait()
    ws_client_task = asyncio.create_task(ws_client.connect_to_server())
    await asyncio.gather(
        prompt.run(),
        driver.run()
    )
    ws_client_task.cancel()
    await ws_server.stop()
    ws_server_task.cancel()

if __name__ == '__main__':
    asyncio.run(main())