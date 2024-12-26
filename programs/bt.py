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
    if len(pixels.controllers) == 0:
        print("No controller connected")
        return

    def handle_event(event, device):
        print(event, device)

    pixels.listen_controllers(handle_event)

    await inquirer.text(message="Press Enter to quit\n").execute_async()
    pixels.stop_listening_controllers()