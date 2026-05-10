class _DriverProxy:
    def __init__(self):
        self._delegate = None

    def set_delegate(self, delegate):
        self._delegate = delegate

    def __getattr__(self, name):
        if self._delegate is None:
            raise AttributeError("Driver has not been initialized")
        return getattr(self._delegate, name)

    def __bool__(self):
        return self._delegate is not None

    def __repr__(self):
        return f"<DriverProxy delegate={self._delegate!r}>"


driver = _DriverProxy()
motion_driver = _DriverProxy()
driver_name = None


def init(driverName, controllerDriverName, motionDriverName):
    global driver_name

    driver_name = driverName

    if driverName == "neopixel":
        from drivers.neopixel.neopixeldriver import NeopixelDriver

        selected_driver = NeopixelDriver()
    elif driverName == "pygame":
        if controllerDriverName == "gamepad":
            from drivers.pygame.gamepad import PygameGamepadDriver

            selected_driver = PygameGamepadDriver()
        else:
            from drivers.pygame.keyboard import PygameKeyboardDriver

            selected_driver = PygameKeyboardDriver()
    else:
        raise Exception(f"Unknown driver: {driverName}")

    if motionDriverName == "pir":
        from drivers.motion_drivers.pir import PirMotionDriver

        selected_motion_driver = PirMotionDriver()
    elif motionDriverName == "file":
        from drivers.motion_drivers.file import FileMotionDriver

        selected_motion_driver = FileMotionDriver()
    else:
        raise Exception(f"Unknown motion driver: {motionDriverName}")

    driver.set_delegate(selected_driver)
    motion_driver.set_delegate(selected_motion_driver)
