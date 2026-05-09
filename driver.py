import config

if config.driver == "neopixel":
    from drivers.neopixel.neopixeldriver import NeopixelDriver
    driver = NeopixelDriver()
elif config.driver == "pygame":
    if config.controller == "gamepad":
        from drivers.pygame.gamepad import PygameGamepadDriver
        driver = PygameGamepadDriver()
    else:
        from drivers.pygame.keyboard import PygameKeyboardDriver
        driver = PygameKeyboardDriver()
else:
    raise Exception(f"Unknown driver: {config.driver}")


if config.motion_driver == "pir":
    from drivers.motion_drivers.pir import PirMotionDriver
    motion_driver = PirMotionDriver()
elif config.motion_driver == "file":
    from drivers.motion_drivers.file import FileMotionDriver
    motion_driver = FileMotionDriver()
else:
    raise Exception(f"Unknown motion driver: {config.motion_driver}")