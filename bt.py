from evdev import InputDevice, ecodes, categorize
import asyncio

event_queue = asyncio.Queue()

async def listen_events():
    gamepad = InputDevice('/dev/input/event2')
    async for event in gamepad.async_read_loop():
        if event.type == ecodes.EV_KEY:
            await event_queue.put(categorize(event))

async def log_events():
    while True:
        event = await event_queue.get()
        print(event)
        event_queue.task_done()

async def main():
    await asyncio.gather(
        listen_events(),
        log_events()
    )

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Programme arrêté.")