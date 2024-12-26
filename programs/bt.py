from InquirerPy import inquirer
from pixels import pixels
from drivers.event_queue import queue
import asyncio

async def connectController():
    devices = pixels.list_devices()
    if len(devices) == 0:
        print("No controller found")
        return
    
    choices = [{
        'value': device,
        'name': pixels.get_device_name(device)
    } for device in devices]

    device = await inquirer.select(
        message="Controller:",
        choices=choices,
    ).execute_async()

    pixels.add_controller(device)

async def testController():
    async def monitor():
        try:
            while True:
                event = await queue.get()
                print(event)
                queue.task_done()
        except asyncio.CancelledError:
            pass

    monitor_task = asyncio.create_task(monitor())

    await inquirer.text(message="Press Enter to quit\n").execute_async()
    monitor_task.cancel()