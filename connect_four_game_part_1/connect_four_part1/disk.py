# Gambhir Kunwar
# 03/29/2020


class Disk:
    """A disk"""
    def __init__(self, SPACE, SLOT_SIZE, COLOR):
        self.SPACE = SPACE
        self.hover = False
        self.fall = False
        self.settled = False
        self.COLOR = COLOR
        self.x = 0
        self.y = 0
        self.width = SLOT_SIZE
        self.height = SLOT_SIZE
        self.SPEED = 5

    def hovering(self):
        """boolean true for hovering state"""
        self.hover = True
        self.fall = False
        self.settled = False

    def falling(self):
        """boolean true for falling state"""
        self.hover = False
        self.fall = True
        self.settled = False

    def settling(self):
        """boolean true for settling state"""
        self.hover = False
        self.fall = False
        self.settled = True

    def display(self):
        """display the disk"""
        fill(*self.COLOR)
        strokeWeight(0)
        ellipse(self.x, self.y, self.width, self.height)
