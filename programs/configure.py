from InquirerPy import inquirer
from pixels import config, reset

def run():
    config['n'] = int(inquirer.number(
        message="Enter number of pixels:",
        default=config['n'],
        min_allowed=1,
    ).execute())

    config['brightness'] = float(inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=config['brightness'],
        min_allowed=0,
    ).execute())

    reset()