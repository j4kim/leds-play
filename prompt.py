from InquirerPy import inquirer
import programs

def run():
    f = None
    while True:
        f = inquirer.select(
            message="Program:",
            choices=programs.choices,
            default=lambda _ : f
        ).execute()
        f()