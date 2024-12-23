from . import configure, individual, cursor, screen, zigzag, text
from pixels import pixels
from config import driver

all = [
    {'value': pixels.fill, 'name': 'Fill', 'only-for': 'neopixel'},
    {'value': pixels.clear, 'name': 'Clear'},
    {'value': text.padscroll_input, 'name': 'Text scroll'},
    {'value': text.minscroll_input, 'name': 'Text min scroll'},
    {'value': text.char, 'name': 'Char'},
    {'value': configure.setFont, 'name': 'Set font'},
    {'value': screen.draw, 'name': 'Draw screen'},
    {'value': screen.fill, 'name': 'Fill screen'},
    {'value': screen.rand, 'name': 'Random screen'},
    {'value': screen.animate, 'name': 'Animate random'},
    {'value': zigzag.horizontal, 'name': 'H Zigzag'},
    {'value': zigzag.vertical, 'name': 'V Zigzag', 'only-for': 'neopixel'},
    {'value': configure.setBrighness, 'name': 'Set brightness', 'only-for': 'neopixel'},
    {'value': configure.setDefaultColor, 'name': 'Set default color'},
    {'value': individual.run, 'name': 'Individual', 'only-for': 'neopixel'},
    {'value': cursor.run, 'name': 'Cursor', 'only-for': 'neopixel'},
]

choices = [p for p in all if not 'only-for' in p or p['only-for'] == driver]