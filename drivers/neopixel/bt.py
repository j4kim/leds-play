import evdev
import asyncio

bindings = {
    '/dev/input/event2': {
        46: 'arrow_up',
        33: 'arrow_right',
        32: 'arrow_down',
        18: 'arrow_left',
        35: 'north',
        34: 'east',
        36: 'south',
        23: 'west',
        37: 'left',
        50: 'right',
        49: 'select',
        24: 'start',
    }
}

def list_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices() if path not in ['/dev/input/event0', '/dev/input/event1']]
    for device in devices:
        print(device.path, device.name, device.phys)

def test_device(path = '/dev/input/event2'):
    gamepad = evdev.InputDevice(path)

    for event in gamepad.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if (event.value == 1):
                print(bindings[path][event.code])

event_queue = asyncio.Queue()

async def listen(path = '/dev/input/event2'):
    gamepad = evdev.InputDevice(path)
    try:
        async for event in gamepad.async_read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                if (event.value == 1):
                    await event_queue.put(bindings[path][event.code])
    except asyncio.exceptions.CancelledError:
        pass
    finally:
        gamepad.close()

async def monitor():
    while True:
        event = await event_queue.get()
        print(event)
        event_queue.task_done()

async def main():
    await asyncio.gather(
        monitor(),
        listen(),
    )

if __name__ == '__main__':
    asyncio.run(main())