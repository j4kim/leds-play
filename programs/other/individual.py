from InquirerPy import inquirer
from driver import driver
from tools import prompt_color

async def run():
    index = await inquirer.number(
        message="Pixel index:",
        max_allowed=driver.n - 1,
        min_allowed=0,
        filter=lambda x: int(x)
    ).execute_async()

    driver.handler[index] = await prompt_color()
    driver.handler.show()
