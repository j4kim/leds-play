import asyncio
import app
import argparse
import driver
from web import ws_server


async def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-p",
        "--program",
        choices=["prompt", "menu", "light"],
        default="prompt",
        help="The program to run",
    )
    parser.add_argument(
        "-d",
        "--driver",
        choices=["pygame", "neopixel"],
        default="pygame",
        help="The LED driver to use",
    )
    parser.add_argument(
        "-c",
        "--controller",
        choices=["keyboard", "gamepad"],
        default="keyboard",
        help="For pygame driver only, the controller driver",
    )
    parser.add_argument(
        "-m",
        "--motion",
        choices=["file", "pir"],
        default="file",
        help="For motion detection driver",
    )
    parser.add_argument(
        "--ws",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Start WebSocket server",
    )
    args = parser.parse_args()
    driver.init(args.driver, args.controller, args.motion)
    if args.ws:
        ws_server_task = asyncio.create_task(ws_server.start())
    await asyncio.gather(app.run(args.program), driver.driver.run())
    await ws_server.stop()
    if args.ws:
        ws_server_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
