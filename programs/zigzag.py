from pixels import pixels
import asyncio

async def horizontal():
    y = 0
    for y in range(7):
        r = range(6)
        if y % 2 == 0:
            r = reversed(range(6))
        for x in r:
            pixels.clear()
            pixels.set(x, y, pixels.default_color)
            pixels.show()
            await asyncio.sleep(0.02)
    pixels.clear()

async def vertical():
    i = 0
    while i < pixels.n:
        pixels.handler.fill(0)
        pixels.handler[i] = pixels.default_color
        pixels.handler.show()
        i += 2
    pixels.clear()