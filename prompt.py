from programs import text, screen, zigzag, configure, individual, cursor, bt, quack, fireworks
from driver import driver
from tools import prompt_menu

async def run():
    await prompt_menu([
        {'value': driver.fill, 'name': 'Fill', 'only-for': 'neopixel'},
        {'value': driver.clear, 'name': 'Clear'},
        {'value': text.menu, 'name': 'Text'},
        {'value': quack.quack, 'name': 'Quack'},
        {'value': fireworks.run, 'name': 'Fireworks'},
        {'value': fireworks.individual, 'name': 'Individual firework'},
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
        {'value': bt.testControllers, 'name': 'Test controllers'},
        {'value': bt.freeThePixel, 'name': 'Free the pixel'},
    ])
    driver.quit()
