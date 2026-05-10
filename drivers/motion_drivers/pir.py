import RPi.GPIO as GPIO


class PirMotionDriver:
    pin = 4

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read(self):
        return GPIO.input(self.pin)

    def quit(self):
        print("PirMotionDriver: GPIO cleanup")
        GPIO.cleanup()
