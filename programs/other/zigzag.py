from driver import driver
import asyncio

async def horizontal():
    y = 0
    for y in range(7):
        r = range(6)
        if y % 2 == 0:
            r = reversed(range(6))
        for x in r:
            driver.clear()
            driver.set(x, y, driver.default_color)
            driver.show()
            await asyncio.sleep(0.02)
    driver.clear()

async def vertical():
    i = 0
    while i < driver.n:
        driver.handler.fill(0)
        driver.handler[i] = driver.default_color
        driver.handler.show()
        i += 2
    driver.clear()