from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import programs

try:
    while True:
        choice = inquirer.select(
            message="Program:",
            choices=[
                Choice(value="fill", name="Fill"),
                Choice(value="deinit", name="Deinit"),
                Choice(value="setpixelnumber", name="Set Pixel Number"),
                Choice(value="setbrightness", name="Set Brightness"),
            ],
        ).execute()
        p = getattr(programs, choice)
        p.run()
except KeyboardInterrupt:
    print("Bye")