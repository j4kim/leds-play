class Handler:
    def show(self):
        print("web Handler show")

class Pixels:
    handler = Handler()

    def reset(self):
        print("web driver reset")

    def __init__(self):
        print("web driver init")

    def fill(self):
        print("web driver fill")

    def clear(self):
        print("web driver clear")

    def set(self, x, y, color):
        print("web driver set", x, y, color)