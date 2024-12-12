import board
import neopixel

def fill(r=255, g=255, b=255):
    pixels = neopixel.NeoPixel(board.D18, 2, brightness=0.1)
    pixels.fill((r, g, b))
    pixels.show()

def deinit():
    pixels = neopixel.NeoPixel(board.D18, 2, brightness=0.1)
    pixels.deinit()
