from flask import session

BOARDID='64ef5905b30edf49e85fa33f'

BOARD_LIST = {
    'To_Do': '64ef5905b30edf49e85fa346', 
    'Doing': '64ef5905b30edf49e85fa347',
    'Done': '64ef5905b30edf49e85fa348'
}

print(BOARD_LIST['To_Do'])