from programs import screen, zigzag, configure, individual, cursor, bt, happynewyear
from driver import driver
from tools import prompt_menu

async def menu():
    await prompt_menu([
        {'value': driver.fill, 'name': 'Fill', 'only-for': 'neopixel'},
        {'value': screen.draw, 'name': 'Draw screen'},
        {'value': screen.fill, 'name': 'Fill screen'},
        {'value': screen.animate, 'name': 'Animate random'},
        {'value': zigzag.horizontal, 'name': 'H Zigzag'},
        {'value': zigzag.vertical, 'name': 'V Zigzag', 'only-for': 'neopixel'},
        {'value': configure.setBrighness, 'name': 'Set brightness'},
        {'value': configure.setDefaultColor, 'name': 'Set default color'},
        {'value': individual.run, 'name': 'Individual', 'only-for': 'neopixel'},
        {'value': cursor.run, 'name': 'Cursor', 'only-for': 'neopixel'},
        {'value': bt.testControllers, 'name': 'Test controllers'},
        {'value': bt.freeThePixel, 'name': 'Free the pixel'},
        {'value': happynewyear.run, 'name': 'Happy New Year'},
        {'value': happynewyear.schedule_for_midnight, 'name': 'Happy New Year (scheduled for midnight)'},
    ])
