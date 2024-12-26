import config

if config.driver == "neopixel":
    from drivers.neopixel.neopixeldriver import NeopixelDriver
    driver = NeopixelDriver()
elif config.driver == "pygame":
    from drivers.pygame.pygamedriver import PygameDriver
    driver = PygameDriver()
else:
    raise Exception(f"Unknown driver: {config.driver}")
