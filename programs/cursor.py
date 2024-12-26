from driver import driver

def run():
    i = 0
    while True:
        if (i >= driver.n):
            i = 0
        driver.handler.fill(0)
        driver.handler[i] = driver.default_color
        driver.handler.show()
        inpt = input(i)
        i = i + 1
        if (inpt == 'q'):
            break
