from programs.happynewyear import fireworks
from driver import driver
from programs.other import bt, configure, cursor, individual, screen, zigzag
from tools import prompt_menu

async def menu():
    await prompt_menu([
        {'value': driver.clear, 'name': 'Clear'},
        {'value': fireworks.individual, 'name': 'Fireworks'},
        {'value': screen.rand, 'name': 'Random screen'},
        {'value': driver.fill, 'name': 'Fill', 'only-for': 'neopixel'},
        {'value': driver.fillscreen, 'name': 'Fill screen'},
        {'value': screen.draw, 'name': 'Draw screen'},
        {'value': screen.animate, 'name': 'Animate random'},
        {'value': zigzag.horizontal, 'name': 'H Zigzag'},
        {'value': zigzag.vertical, 'name': 'V Zigzag', 'only-for': 'neopixel'},
        {'value': configure.setBrighness, 'name': 'Set brightness'},
        {'value': configure.setDefaultColor, 'name': 'Set default color'},
        {'value': individual.run, 'name': 'Individual', 'only-for': 'neopixel'},
        {'value': cursor.run, 'name': 'Cursor', 'only-for': 'neopixel'},
        {'value': bt.testControllers, 'name': 'Test controllers'},
    ])
