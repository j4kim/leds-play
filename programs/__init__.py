from . import configure, individual, cursor, screen, zigzag
from pixels import pixels

list = [
    {'value': pixels.fill, 'name': 'Fill'},
    {'value': pixels.clear, 'name': 'Clear'},
    {'value': screen.draw, 'name': 'Draw screen'},
    {'value': screen.fill, 'name': 'Fill screen'},
    {'value': screen.rand, 'name': 'Random screen'},
    {'value': screen.animate, 'name': 'Animate random'},
    {'value': zigzag.horizontal, 'name': 'H Zigzag'},
    {'value': zigzag.vertical, 'name': 'V Zigzag'},
    {'value': configure.setBrighness, 'name': 'Set brightness'},
    {'value': configure.setDefaultColor, 'name': 'Set default color'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': cursor.run, 'name': 'Cursor'},
]