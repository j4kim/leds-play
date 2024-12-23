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
    programs.text.default_font_index = inquirer.number(
        message="Default font:",
        min_allowed=0,
        max_allowed=len(programs.text.fonts) - 1,
        filter=lambda x: int(x),
        default=programs.text.default_font_index
    ).execute()

def setTextFps():
    programs.text.default_fps = inquirer.number(
        message="Defaut text fps:",
        min_allowed=1,
        max_allowed=30,
        filter=lambda x: int(x),
        default=programs.text.default_fps
    ).execute()