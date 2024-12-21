from InquirerPy import inquirer
import programs

async def run():
    f = None
    while True:
        f = await inquirer.select(
            message="Program:",
            choices=programs.choices,
            default=lambda _ : f
        ).execute_async()
        f()