import asyncio
from .. import text
from .. import fireworks
from web import ws_server
from .. import screen
from InquirerPy import inquirer
from driver import driver
import datetime
from InquirerPy.utils import patched_print

async def fireworks_1():
    await fireworks.fire(0)
    await fireworks.fire(1)

async def fireworks_2():
    await fireworks.fire(2)
    await fireworks.fire(3)
    await fireworks.fire(4)

async def fireworks_3():
    await fireworks.fire(3)
    await fireworks.fire(5)
    await fireworks.fire(1)

async def fireworks_4():
    await fireworks.fire(6)

async def fireworks_5():
    await fireworks.fire(7)
    ws_server.playsound("halala")
    await fireworks.fire(0)
    await fireworks.fire(8)
    await fireworks.fire(6)

async def fireworks_6():
    await fireworks.fire(5)
    await fireworks.fire(4)
    ws_server.playsound("wow c'est beau")
    await fireworks.fire(0)
    await fireworks.fire(3)
    await fireworks.fire(9)

async def countdown():
    ws_server.playsound("10-9-8")
    for i in range(10, 0, -1):
        asyncio.create_task(text.tools.minscroll(str(i)))
        await asyncio.sleep(1)
    ws_server.setvolume("good times", 0.4)
    ws_server.playsound("good times")
    for i in range(4):
        text.tools.char("0", colors=(0xeeaaff, 0x220000))
        await asyncio.sleep(0.2)
        text.tools.char("0", colors=(0xffeeaa, 0x110011))
        await asyncio.sleep(0.2)

async def bonne_annee():
    ws_server.playsound("bonne année")
    await text.tools.funky(
        text.tools.padscroll,
        "Bonne année!",
        ((0xffffff, 0x000808), (0xffffff, 0x080800)),
        multiplier=8
    )

async def happy_new_year():
    ws_server.playsound("happy new year")
    await text.tools.funky(
        text.tools.minscroll,
        "Happy New Year!",
        ((0xcc00ff, 0x080100), (0xff00cc, 0x010008)),
        font_index=5
    )

async def deux_zero_deux_cinq():
    ws_server.playsound("2-0-2-5")
    text.tools.char("2", colors=(0xffff00, 0x000011))
    await asyncio.sleep(1)
    text.tools.char("0", colors=(0xff00ff, 0x001100))
    await asyncio.sleep(1)
    text.tools.char("2", colors=(0x00ffff, 0x110000))
    await asyncio.sleep(1)
    text.tools.char("5", colors=(0xff9944, 0x000011))
    await asyncio.sleep(1)

async def deux_mille_25():
    ws_server.playsound("2025")
    await text.tools.funky(
        text.tools.padscroll,
        "2025",
        ((0xffffff, 0x090909), (0xffff88, 0)),
        multiplier=8
    )

async def la_sante():
    ws_server.playsound("la santé")
    await text.tools.funky(
        text.tools.padscroll,
        "la santé",
        ((0x00ccff, 0x030003), (0x00ffcc, 0x000303)),
        font_index=5
    )

async def random_disco(steps = 4, bpm = 111, multiplier = 2):
    bps = bpm/60
    fps = bps * multiplier
    for i in range(steps):
        screen.rand()
        await asyncio.sleep(1/fps)

async def tchin_tchin():
    ws_server.playsound("tchin-tchin")
    await text.tools.funky(
        text.tools.padscroll,
        "tchin-tchin",
        ((0, 0x999900), (0, 0x009999)),
        font_index=5,
        multiplier=8
    )

async def fireworks_final():
    driver.clear()
    ws_server.fade("good times", 0.4, 0, 8000)
    await asyncio.sleep(8)
    ws_server.pausesound("good times")
    await fireworks.fire(10)
    driver.clear()
    await asyncio.sleep(2)

async def fadeout():
    ws_server.setvolume("good times", 0.6)
    ws_server.resumesound("good times")
    ws_server.fade("good times", 0.6, 0, 50000)
    x = 100
    while x >= 0:
        await random_disco()
        x -= 2
        driver.brightness = x/100
        driver.reset()
    driver.brightness = 1
    driver.reset()

async def start():
    await countdown()
    await fireworks_1()
    await bonne_annee()
    await fireworks_2()
    await happy_new_year()
    await fireworks_3()
    await deux_zero_deux_cinq()
    await fireworks_4()
    await deux_mille_25()
    await fireworks_5()
    await la_sante()
    await random_disco(12)
    await fireworks_6()
    await tchin_tchin()
    await random_disco(32, multiplier=4)
    await fireworks_final()
    await fadeout()

async def scheduled_start(dt):
    patched_print("schedule start at", dt)
    while True:
        now = datetime.datetime.now()
        delta = dt - now
        delay = delta.total_seconds()
        if delay < 60:
            ws_server.playsound("ding")
            patched_print(now, "starting in", delay, "seconds")
            await asyncio.sleep(delay)
            await start()
            return
        if 90 < delay < 120:
            ws_server.playsound("ding")
        patched_print(now, "start in", delta)
        await asyncio.sleep(30)

async def start_at(dt):
    task = asyncio.create_task(scheduled_start(dt))
    await inquirer.text(message="Task scheduled, Enter to cancel").execute_async()
    task.cancel()
    driver.clear()
    ws_server.stopsounds()

async def schedule_for_midnight():
    now = datetime.datetime.now()
    next_day = now + datetime.timedelta(days=1)
    midnight = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
    ten_sec_before = midnight - datetime.timedelta(seconds=10)
    await start_at(ten_sec_before)

async def run():
    await start_at(datetime.datetime.now())
