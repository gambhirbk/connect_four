# Gambhir Kunwar
# 04/15/2020


class Board:
    """A game board is created"""
    def __init__(self, SPACE, ROWS_NO, COLUMNS_NO, SLOT_SIZE):
        self.SPACE = SPACE
        self.ROWS_NO = ROWS_NO
        self.COLUMNS_NO = COLUMNS_NO
        self.SLOT_SIZE = SLOT_SIZE
        self.STROKE_LINE = SLOT_SIZE/12
        self.STROKE_COLOR = (0, 0, 200)

    def display(self):
        """display a board"""
        strokeWeight(self.STROKE_LINE)
        stroke(*self.STROKE_COLOR)
        # loop to draw vertical squares
        for v in range(self.COLUMNS_NO + 1):
            increment = v * self.SLOT_SIZE
            line(increment, self.SLOT_SIZE, increment, self.SPACE['h'])
        # loop to draw horizontal squares
        for h in range(self.ROWS_NO + 1):
            increment = h * self.SLOT_SIZE
            line(0, self.SLOT_SIZE + increment,
                 self.SPACE['w'], self.SLOT_SIZE + increment)
