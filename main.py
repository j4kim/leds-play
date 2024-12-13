from InquirerPy import inquirer
import programs

f = programs.list[0]['value']

try:
    while True:
        f = inquirer.select(
            message="Program:",
            choices=programs.list,
            default=lambda _ : f
        ).execute()
        f()
except KeyboardInterrupt:
    print("Bye")