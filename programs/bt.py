from InquirerPy import inquirer
from pixels import pixels

async def testControllers():
    def handle_event(event):
        print(event)

    pixels.listen_controllers(handle_event)

    await inquirer.text(message="Press Enter to quit\n").execute_async()
    pixels.stop_listening_controllers()