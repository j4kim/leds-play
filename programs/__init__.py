from . import configure, individual, cursor, screen
from pixels import pixels

list = [
    {'value': pixels.fill, 'name': 'Fill'},
    {'value': pixels.clear, 'name': 'Clear'},
    {'value': screen.run, 'name': 'Screen'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': configure.run, 'name': 'Configure'},
    {'value': cursor.run, 'name': 'Cursor'},
]