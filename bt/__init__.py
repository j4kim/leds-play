import evdev

def list_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)

def test_device(path = '/dev/input/event2'):
    gamepad = evdev.InputDevice(path)

    for event in gamepad.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if (event.value == 1):
                print(event.code)