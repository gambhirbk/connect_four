# Gambhir Kunwar
# 03/29/2020

from board import Board
from disk import Disk


class GameManager:
    """
    Maintains the state of the game
    and manages interactions of game elements
    """

    def __init__(self, SPACE, ROWS_NO, COLUMNS_NO, SLOT_SIZE):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.ROWS_NO = ROWS_NO
        self.COLUMNS_NO = COLUMNS_NO
        self.SLOT_SIZE = SLOT_SIZE
        self.game_on_progress = False
        self.player_turn_to_play = False
        self.game_ended = False
        self.RED = (255, 0, 0)
        
        self.board = Board(self.SPACE, self.ROWS_NO, self.COLUMNS_NO,
                           self.SLOT_SIZE)
        self.list_of_disk = []
        # numpy could have been easier to use
        # numpy was supported by processing
        self.array_disk = [[0] * self.COLUMNS_NO for i in range(self.ROWS_NO)]
        self.index_of_row = 0
        self.index_of_column = 0
        self.no_of_empty_slots = [0] * self.COLUMNS_NO
        self.counter_of_empty_slots = [0] * self.COLUMNS_NO
        self.height_of_stacked_disk = 0

    def update(self):
        DIVIDER_FOR_DISK_AXIS = 2
        """updates game state on every frame"""
        # Display board at beginning of the game
        if self.game_on_progress is False and self.game_ended is False:
            self.board.display()

        for row in self.array_disk:
            for column in range(len(row)):
                if type(row[column]) == int:
                    self.counter_of_empty_slots[column] += 1
        self.no_of_empty_slots = self.counter_of_empty_slots
        self.counter_of_empty_slots = [0] * self.COLUMNS_NO

        # Drop and display list of disk
        for disk in self.list_of_disk:

            # hover triggered by mouse click
            if disk.hover is True:
                disk.x = mouseX
                disk.y = self.SLOT_SIZE/DIVIDER_FOR_DISK_AXIS

            # Falling triggered by mouse release
            elif disk.fall is True:
                # Array indexes
                self.index_of_column = disk.x//self.SLOT_SIZE
                self.index_of_row = self.no_of_empty_slots[
                                    self.index_of_column] - 1
                # Disk positioning
                disk.x = ((disk.x//self.SLOT_SIZE) * self.SLOT_SIZE
                          + self.SLOT_SIZE/DIVIDER_FOR_DISK_AXIS)
                disk.y = disk.y + disk.SPEED
                # stop moving the disk at certain height and add to array
                self.height_of_stacked_disk = (self.no_of_empty_slots[
                                          self.index_of_column] *
                                          self.SLOT_SIZE +
                                          self.SLOT_SIZE/DIVIDER_FOR_DISK_AXIS)
                if disk.y == self.height_of_stacked_disk:
                    disk.settling()
                    self.array_disk[
                        self.index_of_row][self.index_of_column] = disk

                # display disks hovering and falling
            disk.display()

        # display board after dist_list has fallen
        self.board.display()

        # check for win
        if self.no_of_empty_slots == [0] * self.COLUMNS_NO:
            self.game_ended = True
            print("Game Over")
            noLoop()

    def handle_mousepress(self):
        """after the mouse is clicked, a disk is added to the list of disk
        and goes into the hover state. This is possible only  when there
        is no disk on the game board or the previous disk is already
        settled down to make sure it has landed."""

        if self.list_of_disk == [] or self.list_of_disk[-1].settled is True:
            self.game_on_progress = True
            # Player 0 has red chip
            if self.player_turn_to_play is False:
                self.list_of_disk.append(Disk(self.SPACE, self.SLOT_SIZE,
                                         self.RED))

                self.list_of_disk[-1].hovering()
            # Player 1 has yellow chip
            if self.player_turn_to_play is True:
                self.list_of_disk.append(Disk(self.SPACE, self.SLOT_SIZE,
                                         self.YELLOW))
                self.list_of_disk[-1].hovering()

    def handle_mouserelease(self):
        """ after relasing the mouse button, the disk goes into falling state
        and players switch their turns. this is possible only when the current
        column is not full of disks and current disks continues to remain
        in the hover state """

        if (self.list_of_disk[-1].hover is True
           and self.no_of_empty_slots[mouseX/self.SLOT_SIZE] != 0):
            self.list_of_disk[-1].falling()
            if self.player_turn_to_play is False:
                self.player_turn_to_play = True
            else:
                self.player_turn_to_play = False
