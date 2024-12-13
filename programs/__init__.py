from . import configure, fill, deinit, individual

list = [
    {'value': fill.run, 'name': 'Fill'},
    {'value': individual.run, 'name': 'Individual'},
    {'value': deinit.run, 'name': 'Deinit'},
    {'value': configure.run, 'name': 'Configure'},
]