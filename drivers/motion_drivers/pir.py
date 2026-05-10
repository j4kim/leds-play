import RPi.GPIO as GPIO
import asyncio
from InquirerPy.utils import patched_print


class PirMotionDriver:
    pin = 4
    initialized = False

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    async def initialize(self):
        if not self.initialized:
            patched_print("Initialisation du capteur PIR...")
            await asyncio.sleep(30)
            patched_print("Capteur initialisé")
            self.initialized = True

    def read(self):
        return GPIO.input(self.pin)

    def quit(self):
        print("PirMotionDriver: GPIO cleanup")
        GPIO.cleanup()
