from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import programs

try:
    while True:
        program = inquirer.select(
            message="Program",
            choices=[
                Choice(value=programs.fill, name="Fill"),
                Choice(value=programs.deinit, name="Deinit"),
                Choice(value=programs.setPixelNumber, name="Set Pixel Number"),
                Choice(value=programs.setBrightness, name="Set Brightness"),
            ],
        ).execute()
        program()
except KeyboardInterrupt:
    print("Bye")