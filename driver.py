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
elif config.driver == "web":
    from drivers.web.webdriver import WebDriver
    driver = WebDriver()
else:
    raise Exception(f"Unknown driver: {config.driver}")
