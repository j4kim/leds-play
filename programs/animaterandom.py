import time
from programs import randomscreen

def run():
    try:
        while True:
            randomscreen.run()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
