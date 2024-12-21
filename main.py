import asyncio
import prompt

async def main():
    await asyncio.gather(prompt.run())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye")