from programs import text, screen, fireworks, other
from programs.games import snake, quack, menu, paint
from driver import driver
from tools import prompt_menu

async def run():
    await prompt_menu([
        {'value': menu.Menu.run, 'name': 'Game menu'},
        {'value': snake.Snake.run, 'name': 'Snake'},
        {'value': quack.Quack.run, 'name': 'Quack'},
        {'value': paint.Paint.run, 'name': 'Paint'},
        {'value': driver.clear, 'name': 'Clear'},
        {'value': text.menu, 'name': 'Text'},
        {'value': fireworks.individual, 'name': 'Fireworks'},
        {'value': screen.rand, 'name': 'Random screen'},
        {'value': other.menu, 'name': 'Other'},
    ])
    driver.quit()
