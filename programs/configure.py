from InquirerPy import inquirer
from pixels import pixels
from tools import prompt_color
import programs.text

async def setBrighness():
    pixels.brightness = await inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=pixels.brightness,
        min_allowed=0,
        filter=lambda x: float(x),
    ).execute_async()
    pixels.reset()

async def setDefaultColor():
    pixels.default_color = await prompt_color("Default color:")

async def setFont():
    programs.text.default_font_index = await inquirer.number(
        message="Default font:",
        min_allowed=0,
        max_allowed=len(programs.text.fonts) - 1,
        filter=lambda x: int(x),
        default=programs.text.default_font_index
    ).execute_async()

async def setTextFps():
    programs.text.default_fps = await inquirer.number(
        message="Defaut text fps:",
        min_allowed=1,
        max_allowed=30,
        filter=lambda x: int(x),
        default=programs.text.default_fps
    ).execute_async()