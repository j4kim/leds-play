import programs
from driver import driver
from tools import prompt_menu

async def run():
    await prompt_menu(programs.choices)
    driver.quit()
