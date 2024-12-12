import board
import neopixel
from InquirerPy import inquirer

pixels = neopixel.NeoPixel(board.D18, 2, brightness=0.1, auto_write=False)

program = inquirer.select(
    message="Program",
    choices=["fill", "deinit"],
).execute()

if program == "fill":
    pixels.fill((255, 255, 255))
    pixels.show()
elif program == "deinit":
    pixels.deinit()
