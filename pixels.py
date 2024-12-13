import board
import neopixel

config = {
    "pin": board.D18,
    "n": 2,
    "brightness": 0.1
}

print("init pixels")
pixels = neopixel.NeoPixel(**config)

def reset():
    global pixels
    pixels = neopixel.NeoPixel(**config)