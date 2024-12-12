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
            ],
        ).execute()
        program()
except KeyboardInterrupt:
    print("Bye")