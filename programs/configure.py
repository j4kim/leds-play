from InquirerPy import inquirer
from pixels import pixels
from tools import prompt_color

def run():
    pixels.n = int(inquirer.number(
        message="Enter number of pixels:",
        default=pixels.n,
        min_allowed=1,
    ).execute())

    pixels.brightness = float(inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=pixels.brightness,
        min_allowed=0,
    ).execute())

    pixels.default_color = prompt_color("Default color:", pixels.default_color)

    pixels.reset()