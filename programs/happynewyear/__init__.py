import asyncio
from .. import text
from .. import fireworks
from web import ws_server

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

    await asyncio.sleep(2)
    ws_server.stopsounds()


