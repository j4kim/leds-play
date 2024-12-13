from . import fill, deinit, setpixelnumber, setbrightness

def list():
    return [
        {'value': fill.run, 'name': 'Fill'},
        {'value': deinit.run, 'name': 'Deinit'},
        {'value': setpixelnumber.run, 'name': 'Set pixel number'},
        {'value': setbrightness.run, 'name': 'Set brightness'},
    ]