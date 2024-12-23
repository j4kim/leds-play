from InquirerPy import inquirer
from pixels import pixels
from tools import prompt_color
import programs.text

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

def setFont():
    programs.text.selected_font_index = inquirer.number(
        message="Font:",
        min_allowed=0,
        max_allowed=len(programs.text.fonts) - 1,
        filter=lambda x: int(x),
        default=programs.text.selected_font_index
    ).execute()