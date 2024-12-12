from InquirerPy import inquirer
import programs

try:
    while True:
        choice = inquirer.select(
            message="Program",
            choices=['fill', 'deinit'],
        ).execute()
        getattr(programs, choice)()
except KeyboardInterrupt:
    print("Bye")