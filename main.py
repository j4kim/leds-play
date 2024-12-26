import asyncio
import prompt
from driver import driver

async def main():
    await asyncio.gather(
        prompt.run(),
        driver.run()
    )

if __name__ == '__main__':
    asyncio.run(main())