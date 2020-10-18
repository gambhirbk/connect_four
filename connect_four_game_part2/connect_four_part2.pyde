# Gambhir Kunwar
# 04/15/2020

""""
.pyde file set ups the screen and calls for draw function and
also calls for mousePressed and mouseReleased function
"""

from game_manager import GameManager

ROWS_NO = 6
COLUMNS_NO = 7
SLOT_SIZE = 100
# SPACE is a dictionary
SPACE = {'w': COLUMNS_NO * SLOT_SIZE, 'h': (ROWS_NO * SLOT_SIZE) + SLOT_SIZE}
LIGHT_GREY = (205, 205, 205)

game_manager = GameManager(ROWS_NO, COLUMNS_NO, SPACE, SLOT_SIZE)


def setup():
    size(SPACE['w'], SPACE['h'])
    name = input('enter your name')
    if name:
        print('hi ' + name)
    elif name == '':
        print('[empty string]')
    else:
        # dialog canceled with print None
        print(name)
    game_manager.name = name


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    background(*LIGHT_GREY)
    game_manager.update()


def mousePressed():
    game_manager.handle_mousepress()


def mouseReleased():
    game_manager.handle_mouserelease()
