from pixels import pixels

def run():
    for i in range(pixels.n):
        print(i, end=": ")
        if sum(pixels.handler[i]) == 0:
            print()
        else:
            print(pixels.handler[i])
