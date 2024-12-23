import asyncio
import prompt
import pixels

async def main():
    await asyncio.gather(
        prompt.run(),
        pixels.pixels.run()
    )

if __name__ == '__main__':
    asyncio.run(main())