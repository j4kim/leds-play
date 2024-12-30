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
        text.tools.char("0", colors=(0xffffff, 0x880000))
        await asyncio.sleep(0.2)
        text.tools.char("0", colors=(0xffffff, 0x440044))
        await asyncio.sleep(0.2)

    await fireworks.fire(0)
    await fireworks.fire(1)

    ws_server.playsound("bonne année")
    await text.tools.funky(
        text.tools.padscroll,
        "Bonne année!",
        ((0xffffff, 0x005522), (0xffffff, 0x002255)),
        multiplier=8
    )

    await fireworks.fire(2)
    await fireworks.fire(3)
    await fireworks.fire(4)

    ws_server.playsound("happy new year")
    await text.tools.funky(
        text.tools.minscroll,
        "Happy New Year!",
        ((0xbb00ff, 0x220011), (0xff00bb, 0x110022)),
        font_index=5
    )

    await fireworks.fire(3)
    await fireworks.fire(5)
    await fireworks.fire(1)

    await asyncio.sleep(2)
    ws_server.stopsounds()


