from InquirerPy import inquirer
import programs

try:
    while True:
        f = inquirer.select(
            message="Program:",
            choices=programs.list()
        ).execute()
        f()
except KeyboardInterrupt:
    print("Bye")