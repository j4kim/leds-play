from programs import text, happynewyear
from programs.games import menu, snake, quack, paint
from programs.other import submenu
from driver import driver
from tools import prompt_menu

async def run():
    await prompt_menu([
        {'value': menu.Menu.run, 'name': 'Game menu'},
        {'value': snake.Snake.run, 'name': 'Snake'},
        {'value': quack.Quack.run, 'name': 'Quack'},
        {'value': paint.Paint.run, 'name': 'Paint'},
        {'value': text.menu, 'name': 'Text'},
        {'value': happynewyear.run, 'name': 'Happy New Year'},
        {'value': submenu.menu, 'name': 'Other'},
    ])
    driver.quit()
