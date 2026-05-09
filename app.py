import config
import prompt
from programs.games import menu
from driver import driver


async def run():
    if config.program == "prompt":
        await prompt.run()
    elif config.program == "menu":
        await menu.Menu.run()
    driver.quit()
