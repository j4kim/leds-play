import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 2, brightness=0.1, auto_write=False)

pixels.fill((10, 10, 10))
pixels.show()


