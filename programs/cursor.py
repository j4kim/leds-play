from pixels import pixels

def run():
    i = 0
    while True:
        if (i >= pixels.n):
            i = 0
        pixels.handler.fill(0)
        pixels.handler[i] = 0xffffff
        inpt = input(i)
        i = i + 1
        if (inpt == 'q'):
            break
