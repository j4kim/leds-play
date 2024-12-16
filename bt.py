from evdev import InputDevice, ecodes, categorize

gamepad = InputDevice('/dev/input/event2')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))