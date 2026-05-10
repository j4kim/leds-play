import config
import prompt
from programs.games import menu
from programs import light
from driver import driver, motion_driver


async def run():
    try:
        if config.program == "prompt":
            await prompt.run()
        elif config.program == "menu":
            await menu.Menu.run()
        elif config.program == "light":
            await light.Light.run()
        else:
            print(f"configured program ({config.program}) not found")
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()
        motion_driver.quit()
