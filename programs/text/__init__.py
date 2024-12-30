import urllib.request
import json
from InquirerPy import inquirer
from . import config
from tools import prompt_menu
from . import tools

async def menu():
    await prompt_menu([
        {'value': padscroll_input, 'name': 'Text scroll'},
        {'value': minscroll_input, 'name': 'Text min scroll'},
        {'value': lambda: funkyminscroll('Happy New Year!'), 'name': 'Funky min scroll'},
        {'value': char_input, 'name': 'Char'},
        {'value': random_word, 'name': 'Random word'},
        {'value': setFont, 'name': 'Set default font'},
        {'value': setTextFps, 'name': 'Set default text fps'},
    ])

async def padscroll_input():
    await tools.padscroll(input("Text: "))

async def funkyminscroll(text, bpm = 111):
    def getcolor(i):
        return (0xffffff, 0x005522) if (i//4) % 2 == 0 else (0xffffff, 0x002255)
    await tools.minscroll(text, 4*(bpm/60), 2, getcolor)

async def minscroll_input():
    await tools.minscroll(input("Text: "))

def char_input():
    tools.char(input("Char: "))

async def random_word():
    data = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?lang=fr&length=5").read().decode("utf-8")
    word = json.loads(data)[0]
    await tools.padscroll(word)
    print(word)

async def setFont():
    config.default_font_index = await inquirer.number(
        message="Default font:",
        min_allowed=0,
        max_allowed=len(config.fonts) - 1,
        filter=lambda x: int(x),
        default=config.default_font_index
    ).execute_async()

async def setTextFps():
    config.default_fps = await inquirer.number(
        message="Defaut text fps:",
        min_allowed=1,
        max_allowed=30,
        filter=lambda x: int(x),
        default=config.default_fps
    ).execute_async()