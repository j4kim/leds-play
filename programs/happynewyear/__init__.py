import asyncio
from .. import text
from .. import fireworks
from web import ws_server
from .. import screen

async def run():
    ws_server.playsound("10-9-8")

    for i in range(10, 0, -1):
        asyncio.create_task(text.tools.minscroll(str(i)))
        await asyncio.sleep(1)

    ws_server.playsound("good times")

    for i in range(4):
        text.tools.char("0", colors=(0xeeaaff, 0x220000))
        await asyncio.sleep(0.2)
        text.tools.char("0", colors=(0xffeeaa, 0x110011))
        await asyncio.sleep(0.2)

    await fireworks.fire(0)
    await fireworks.fire(1)

    ws_server.playsound("bonne année")
    await text.tools.funky(
        text.tools.padscroll,
        "Bonne année!",
        ((0xffffff, 0x000808), (0xffffff, 0x080800)),
        multiplier=8
    )

    await fireworks.fire(2)
    await fireworks.fire(3)
    await fireworks.fire(4)

    ws_server.playsound("happy new year")
    await text.tools.funky(
        text.tools.minscroll,
        "Happy New Year!",
        ((0xcc00ff, 0x080100), (0xff00cc, 0x010008)),
        font_index=5
    )

    await fireworks.fire(3)
    await fireworks.fire(5)
    await fireworks.fire(1)

    ws_server.playsound("2-0-2-5")
    text.tools.char("2", colors=(0xffff00, 0x000011))
    await asyncio.sleep(1)
    text.tools.char("0", colors=(0xff00ff, 0x001100))
    await asyncio.sleep(1)
    text.tools.char("2", colors=(0x00ffff, 0x110000))
    await asyncio.sleep(1)
    text.tools.char("5", colors=(0xff9944, 0x000011))
    await asyncio.sleep(1)

    await fireworks.fire(6)

    ws_server.playsound("2025")
    await text.tools.funky(
        text.tools.padscroll,
        "2025",
        ((0xffffff, 0x090909), (0xe0e0e0, 0)),
        multiplier=8
    )

    await fireworks.fire(7)
    ws_server.playsound("halala")
    await fireworks.fire(0)
    await fireworks.fire(8)
    await fireworks.fire(6)

    ws_server.playsound("la santé")
    await text.tools.funky(
        text.tools.padscroll,
        "la santé",
        ((0x00ccff, 0x030003), (0x00ffcc, 0x000303)),
        font_index=5
    )

    for i in range(8):
        screen.rand()
        await asyncio.sleep(0.1)

    await fireworks.fire(5)
    await fireworks.fire(4)
    ws_server.playsound("wow c'est beau")
    await fireworks.fire(0)
    await fireworks.fire(3)
    await fireworks.fire(9)

    ws_server.playsound("tchin-tchin")
    await text.tools.funky(
        text.tools.padscroll,
        "tchin-tchin",
        ((0, 0x999900), (0, 0x009999)),
        font_index=5,
        multiplier=8
    )

    await asyncio.sleep(2)
    ws_server.stopsounds()


