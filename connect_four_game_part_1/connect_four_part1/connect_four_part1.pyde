# Gambhir Kunwar
# 03/29/2020

""""
.pyde file set ups the screen and calls for draw function and
also calls for mousePressed and mouseReleased function
"""

from game_manager import GameManager

ROWS_NO = 2
COLUMNS_NO = 2
SLOT_SIZE = 100
# SPACE is a dictionary
SPACE = {'w': COLUMNS_NO * SLOT_SIZE, 'h': (ROWS_NO * SLOT_SIZE) + SLOT_SIZE}
LIGHT_GREY = (205, 205, 205)

game_manager = GameManager(SPACE, ROWS_NO, COLUMNS_NO, SLOT_SIZE)


def setup():
    size(SPACE['w'], SPACE['h'])


def draw():
    background(*LIGHT_GREY)
    game_manager.update()


def mousePressed():
    game_manager.handle_mousepress()


def mouseReleased():
    game_manager.handle_mouserelease()
