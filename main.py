import asyncio
import prompt
from driver import driver
from web import ws_client

async def main():
    ws_task = asyncio.create_task(ws_client.connect_to_server())
    await asyncio.gather(
        prompt.run(),
        driver.run()
    )
    ws_task.cancel()

if __name__ == '__main__':
    asyncio.run(main())