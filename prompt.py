from InquirerPy import inquirer
import programs
import asyncio

async def run():
    f = None
    while True:
        f = await inquirer.select(
            message="Program:",
            choices=programs.choices,
            default=lambda _ : f
        ).execute_async()
        r = f()
        if asyncio.iscoroutine(r):
            await r
