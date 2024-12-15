from . import configure, fill, individual, reset, list, cursor, screen

list = [
    {'value': fill.run, 'name': 'Fill'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': reset.run, 'name': 'Reset'},
    {'value': list.run, 'name': 'List'},
    {'value': configure.run, 'name': 'Configure'},
    {'value': cursor.run, 'name': 'Cursor'},
    {'value': screen.run, 'name': 'Screen'},
]