from programs import text, screen, quack, fireworks, other, snake
from driver import driver
from tools import prompt_menu

async def run():
    await prompt_menu([
        {'value': snake.run, 'name': 'Snake'},
        {'value': quack.quack, 'name': 'Quack'},
        {'value': driver.clear, 'name': 'Clear'},
        {'value': text.menu, 'name': 'Text'},
        {'value': fireworks.individual, 'name': 'Fireworks'},
        {'value': screen.rand, 'name': 'Random screen'},
        {'value': other.menu, 'name': 'Other'},
    ])
    driver.quit()
