from InquirerPy import inquirer
from config import config

def run():
    config['brightness'] = float(inquirer.number(
        message="Enter Brightness:",
        float_allowed=True,
        default=config['brightness'],
        min_allowed=0,
    ).execute())