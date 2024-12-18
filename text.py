from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_bitmap(text, font_path="PressStart2P-Regular.ttf", size=8):
    font = ImageFont.truetype(font_path, size)
    w = len(text) * size
    image = Image.new("1", (w, size), 0)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=1)
    return np.array_split(list(image.getdata()), size)

values = generate_bitmap("Hello!")

for row in values:
    for x in row:
        print("#" if x else " ", end="|")
    print()