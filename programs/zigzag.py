from pixels import pixels
import time

def run():
    y = 0
    for y in range(7):
        r = range(6)
        if y % 2 == 0:
            r = reversed(range(6))
        for x in r:
            pixels.handler.fill(0)
            pixels.set(x, y, pixels.default_color)
            pixels.handler.show()
            time.sleep(0.02)
    pixels.clear()
