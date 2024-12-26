import evdev

bindings = {
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

def list_devices():
    return [
        evdev.InputDevice(path)
        for path in evdev.list_devices()
        if path not in ['/dev/input/event0', '/dev/input/event1'] # remove hdmi devices
    ]