from . import configure, individual, cursor, screen, fillscreen, randomscreen, animaterandom, zigzag
from pixels import pixels

list = [
    {'value': pixels.fill, 'name': 'Fill'},
    {'value': pixels.clear, 'name': 'Clear'},
    {'value': screen.run, 'name': 'Screen'},
    {'value': fillscreen.run, 'name': 'Fill screen'},
    {'value': randomscreen.run, 'name': 'Random screen'},
    {'value': animaterandom.run, 'name': 'Animate random'},
    {'value': zigzag.run, 'name': 'Zigzag'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': configure.run, 'name': 'Configure'},
    {'value': cursor.run, 'name': 'Cursor'},
]