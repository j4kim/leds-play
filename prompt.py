from InquirerPy import inquirer
import programs
import asyncio
import pixels

async def run():
    f = None
    while pixels.pixels.running:
        f = await inquirer.select(
            message="Program:",
            choices=programs.choices,
            default=lambda _ : f
        ).execute_async()
        r = f()
        if asyncio.iscoroutine(r):
            await r
