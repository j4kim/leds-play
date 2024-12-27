from InquirerPy import inquirer
from driver import driver
from tools import prompt_color

async def setBrighness():
    driver.brightness = await inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=driver.brightness,
        min_allowed=0,
        filter=lambda x: float(x),
    ).execute_async()
    driver.reset()

async def setDefaultColor():
    driver.default_color = await prompt_color("Default color:")
