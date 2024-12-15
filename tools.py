from InquirerPy import inquirer

def prompt_color(message = "hex value or one of r,g,b,w,m,y,c:"):
    color = inquirer.text(message).execute()

    mapping = {
        'r': 'ff0000',
        'g': '00ff00',
        'b': '0000ff',
        'w': 'ffffff',
        'm': 'ff00ff',
        'y': 'ffff00',
        'c': '00ffff',
    }

    if color in mapping:
        color = mapping[color]

    return int(color, 16)