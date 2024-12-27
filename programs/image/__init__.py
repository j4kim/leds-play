from PIL import Image
import os.path
import numpy as np
from pprint import pprint
from driver import driver

def show_image(path):
    path = os.path.join(os.path.dirname(__file__), path)
    image = Image.open(path)
    bitmap = np.array_split(list(image.getdata()), 7)
    for y in range(7):
        for x in range(6):
            driver.set(x, y, bitmap[y][x][:3])
    driver.show()

def duck():
    show_image("duck.png")