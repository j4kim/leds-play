from . import configure, individual, cursor, screen, fillscreen
from pixels import pixels

list = [
    {'value': pixels.fill, 'name': 'Fill'},
    {'value': pixels.clear, 'name': 'Clear'},
    {'value': screen.run, 'name': 'Screen'},
    {'value': fillscreen.run, 'name': 'Fill screen'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': configure.run, 'name': 'Configure'},
    {'value': cursor.run, 'name': 'Cursor'},
]