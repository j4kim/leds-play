from InquirerPy import inquirer
from pixels import pixels
from tools import prompt_color

def setBrighness():
    pixels.brightness = float(inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=pixels.brightness,
        min_allowed=0,
    ).execute())
    pixels.reset()

def setDefaultColor():
    pixels.default_color = prompt_color("Default color:")
