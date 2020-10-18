# Gambhir Kunwar
# 04/15/2020


class Disk:
    """A disk"""
    def __init__(self, SLOT_SIZE, PLAYER, ROW_NO, COLUMN_NO):
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.width = SLOT_SIZE
        self.height = SLOT_SIZE
        self.diam = SLOT_SIZE
        self.PLAYER = PLAYER
        self.ROW_NO = ROW_NO
        self.COLUMN_NO = COLUMN_NO
        self.x = 0
        self.y = 0
        self.hover = 0
        self.fall = 0
        self.settled = 0
        self.SPEED = 5
        self.PLAYER_ONE = 1
        self.PLAYER_TWO = 2

    def display(self):
        """Used to draw the actual disk"""
        strokeWeight(0)
        if self.PLAYER == self.PLAYER_ONE:
            self.color = self.RED
            fill(*self.color)
            ellipse(self.x, self.y, self.width, self.height)

        elif self.PLAYER == self.PLAYER_TWO:
            self.color = self.YELLOW
            fill(*self.color)
            ellipse(self.x, self.y, self.width, self.height)

    def get_x(self, array):
        """Goes over the array and finds first empty spot"""
        for column in range(self.COLUMN_NO):
            for row in range(self.ROW_NO):
                if array[column][row] == 0:
                    x = self.diam * column + self.diam//2
                    return x
