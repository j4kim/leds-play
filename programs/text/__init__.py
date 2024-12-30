import urllib.request
import json
from InquirerPy import inquirer
from . import config
from tools import prompt_menu
from . import tools

async def menu():
    await prompt_menu([
        {'value': padscroll_input, 'name': 'Text scroll'},
        {'value': funkypadscroll, 'name': 'Funky scroll'},
        {'value': minscroll_input, 'name': 'Text min scroll'},
        {'value': funkyminscroll, 'name': 'Funky min scroll'},
        {'value': char_input, 'name': 'Char'},
        {'value': random_word, 'name': 'Random word'},
        {'value': setFont, 'name': 'Set default font'},
        {'value': setTextFps, 'name': 'Set default text fps'},
    ])

async def padscroll_input():
    await tools.padscroll(input("Text: "))

async def funkypadscroll():
    await tools.funky(tools.padscroll, input("Text: "), ((0, 0xff9900), (0, 0xff0099)), font_index=5)

async def minscroll_input():
    await tools.minscroll(input("Text: "))

async def funkyminscroll():
    await tools.funky(tools.minscroll, input("Text: "), ((0xffffff, 0x005522), (0xffffff, 0x002255)))

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