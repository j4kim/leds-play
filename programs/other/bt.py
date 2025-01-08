from InquirerPy import inquirer
from InquirerPy.utils import patched_print
from driver import driver

async def testControllers():
    def handle_event(event):
        patched_print(event)

    try:
        driver.listen_controllers(handle_event)
    except Exception as e:
        patched_print(e)
        return

    await inquirer.text(message="Press Enter to quit").execute_async()
    driver.stop_listening_controllers()
