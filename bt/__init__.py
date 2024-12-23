import evdev

bindings = {
    '/dev/input/event2': {
        46: 'arrow_up',
        33: 'arrow_right',
        32: 'arrow_down',
        18: 'arrow_left',
        35: 'x',
        34: 'a',
        36: 'b',
        23: 'y',
        37: 'left',
        50: 'right',
        49: 'select',
        24: 'start',
    }
}

def list_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)

def test_device(path = '/dev/input/event2'):
    gamepad = evdev.InputDevice(path)

    for event in gamepad.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if (event.value == 1):
                print(bindings[path][event.code])