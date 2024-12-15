from pixels import pixels

def run():
    y = 0
    for y in range(7):
        values = input(f"{y}: ").split()
        for x in range(6):
            try:
                v = values[x]
            except IndexError:
                v = 0
            pixels.set(x, y, v)