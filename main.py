from InquirerPy import inquirer
import programs

f = programs.choices[0]['value']

try:
    while True:
        f = inquirer.select(
            message="Program:",
            choices=programs.choices,
            default=lambda _ : f
        ).execute()
        f()
except KeyboardInterrupt:
    print("Bye")