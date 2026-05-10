import prompt
from programs.games import menu
from programs import light
from driver import driver, motion_driver


async def run(program):
    try:
        if program == "prompt":
            await prompt.run()
        elif program == "menu":
            await menu.Menu.run()
        elif program == "light":
            await light.Light.run()
        else:
            print(f"configured program ({program}) not found")
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()
        motion_driver.quit()
