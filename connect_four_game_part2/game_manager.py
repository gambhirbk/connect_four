# Gambhir Kunwar
# 04/15/2020

from disk import Disk
from board import Board
"""
updates the loop for the draw function in the .pyde file. handles
the game state, player turn, and events.
"""

import math


class GameManager:
    """
    Maintains the state of the game
    and manages interactions of game elements
    """
    def __init__(self, ROW_NO, COLUMN_NO, SPACE, SLOT_SIZE):
        self.ROW_NO = ROW_NO
        self.COLUMN_NO = COLUMN_NO
        self.SPACE = SPACE
        self.SLOT_SIZE = SLOT_SIZE
        self.board = Board(self.SPACE, self.ROW_NO, self.COLUMN_NO,
                           self.SLOT_SIZE)
        self.player = 1
        self.game_start = False
        self.input_start = 0
        self.name = ''
        self.points = 0

        # Positional data.
        self.array = [[0] * self.ROW_NO for i in range(self.COLUMN_NO)]
        self.index_of_row = 0
        self.index_of_column = 0
        self.no_of_empty_slots = [0] * self.COLUMN_NO
        self.row_count = 0
        # Disk storage.
        self.list_of_disk = []
        self.player_turn = True
        self.game_ended = False
        self.can_go = 1
        self.timer = 0
        self.TIME_LIMIT = 100
        self.START_DELAY = 40

    def update(self):
        """updates games state per frame"""
        # To print first player turn message.
        if self.game_start is True:
            print("Player one's turn.")
            self.game_start is False

        # Array with empty slots
        self.check_empty_slots()

        # makes AI and player moves
        self.winning_move()

        # disks for computer apppear
        self.computer_move()

        # Drop and display disk list and record score
        self.show_disks_record_score()

        # display the board after disk drops
        self.board.display()

    def check_empty_slots(self):
        """checks if there is empty spot or not"""
        filled_slots = 0
        for column in range(self.COLUMN_NO):
            self.row_count = 0
            for row in range(self.ROW_NO):
                if self.array[column][row] == 0:
                    self.row_count += 1
                if self.array[column][row] != 0:
                    filled_slots += 1
            # This is a sum for each column, so i can count the zeros and
            # use that as an index
            self.no_of_empty_slots[column] = self.row_count
        # To not allow more disks to be generated than slots.
        if (self.ROW_NO * self.COLUMN_NO) == filled_slots:
            self.game_ended = True
            print("Game Over")

    def winning_move(self):
        """checks for the winning move"""
        # To check four in a row
        NO_WIN_COL = 3  # if there is only 3 sequence possible, no win possibe
        NO_WIN_ROW = 3
        FIRST_IN_SEQ = 1
        SECOND_IN_SEQ = 2
        THIRD_IN_SEQ = 3
        PLAYER_PIECE = 1
        AI_PIECE = 2

        if self.game_ended is False:
            # check vertical locations for win
            for c in range(self.COLUMN_NO):
                for r in range(self.ROW_NO - NO_WIN_ROW):
                    if self.array[c][r] == PLAYER_PIECE and \
                        self.array[c][r + FIRST_IN_SEQ] == PLAYER_PIECE \
                        and self.array[c][r + SECOND_IN_SEQ] == PLAYER_PIECE \
                            and self.array[c][r + THIRD_IN_SEQ] == \
                            PLAYER_PIECE:
                        print("Player 1 wins")
                        self.game_ended = True
                        self.points = 1

                    if self.array[c][r] == AI_PIECE and \
                        self.array[c][r + FIRST_IN_SEQ] == AI_PIECE \
                        and self.array[c][r + SECOND_IN_SEQ] == AI_PIECE \
                            and self.array[c][r + THIRD_IN_SEQ] == AI_PIECE:
                        print("AI wins")
                        self.game_ended = True

            # check horizontal locations for win
            for c in range(self.COLUMN_NO - NO_WIN_COL):
                for r in range(self.ROW_NO):
                    if self.array[c][r] == PLAYER_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r] == PLAYER_PIECE \
                        and self.array[c + SECOND_IN_SEQ][r] == PLAYER_PIECE \
                        and self.array[c + THIRD_IN_SEQ][r] == \
                            PLAYER_PIECE:
                        print("Player 1 wins")
                        self.game_ended = True
                        self.points = 1

                    if self.array[c][r] == AI_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r] == AI_PIECE \
                        and self.array[c + SECOND_IN_SEQ][r] == AI_PIECE \
                        and self.array[c + THIRD_IN_SEQ][r] == \
                            AI_PIECE:
                        print("AI wins")
                        self.game_ended = True

            # check negative slope diagonals
            for c in range(self.COLUMN_NO - NO_WIN_COL):
                for r in range(self.ROW_NO - NO_WIN_ROW):
                    if self.array[c][r] == PLAYER_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r + FIRST_IN_SEQ] \
                        == PLAYER_PIECE and \
                        self.array[c + SECOND_IN_SEQ][r + SECOND_IN_SEQ] \
                        == PLAYER_PIECE \
                        and self.array[c + THIRD_IN_SEQ][r + THIRD_IN_SEQ] \
                            == PLAYER_PIECE:
                        print("Player 1 wins")
                        self.game_ended = True
                        self.points = 1

                    if self.array[c][r] == AI_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r + FIRST_IN_SEQ] \
                        == AI_PIECE and \
                        self.array[c + SECOND_IN_SEQ][r + SECOND_IN_SEQ] \
                        == AI_PIECE and \
                        self.array[c + THIRD_IN_SEQ][r + THIRD_IN_SEQ] \
                            == AI_PIECE:
                        print("AI wins")
                        self.game_ended = True

            # check positive slope diagonal
            for c in range(self.COLUMN_NO - NO_WIN_COL):
                for r in range(NO_WIN_ROW, self.ROW_NO):
                    if self.array[c][r] == PLAYER_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r - FIRST_IN_SEQ] == \
                        PLAYER_PIECE and \
                        self.array[c + SECOND_IN_SEQ][row - SECOND_IN_SEQ] == \
                        PLAYER_PIECE and \
                        self.array[c + THIRD_IN_SEQ][r - THIRD_IN_SEQ] \
                            == PLAYER_PIECE:
                        print("AI wins")
                        self.game_ended = True
                        self.points = 1

                    if self.array[c][r] == AI_PIECE and \
                        self.array[c + FIRST_IN_SEQ][r - FIRST_IN_SEQ] == \
                        AI_PIECE and \
                        self.array[c + SECOND_IN_SEQ][row - SECOND_IN_SEQ] == \
                        AI_PIECE and \
                        self.array[c + THIRD_IN_SEQ][r - THIRD_IN_SEQ] == \
                            AI_PIECE:
                        print("AI wins")
                        self.game_ended = True

    def computer_move(self):
        """AI turn"""
        AI = 2
        if (self.player == AI and self.player_turn is False and self.game_ended
                is False):
            self.timer += 1

            if self.timer == self.START_DELAY:
                disk = Disk(self.SLOT_SIZE, self.player, self.ROW_NO,
                            self.COLUMN_NO)
                self.list_of_disk.append(disk)
                self.list_of_disk[-1].hover = 1
            # Time has passed to drop.
            if self.timer == self.TIME_LIMIT:
                self.player_turn = True
                self.list_of_disk[-1].hover = 0
                self.list_of_disk[-1].fall = 1

    def handle_mousepress(self):
        """Creates a disk, adds to list, and swaps player"""
        if self.player_turn is True and self.game_ended is False:
            if self.player == 1:
                disk = Disk(self.SLOT_SIZE, self.player, self.ROW_NO,
                            self.COLUMN_NO)
                self.list_of_disk.append(disk)
                self.list_of_disk[-1].hover = 1

    def handle_mouserelease(self):
        """When mouse releases it changes the disks state"""
        if self.game_ended is False and self.player == 1:
            self.list_of_disk[-1].hover = 0
            self.list_of_disk[-1].fall = 1
            self.player_turn = False

    def show_disks_record_score(self):
        """shows disks and keeps records"""
        DISK_DIVIDER = 2
        PLAYER_ONE = 1
        PLAYER_TWO = 2
        CONST_TWO = 2
        for disk in self.list_of_disk:
            # Human part.
            if disk.PLAYER == PLAYER_ONE:
                # While holding mouse down.
                if disk.hover == 1:
                    disk.x = (math.floor(mouseX / self.SLOT_SIZE) *
                              self.SLOT_SIZE + (0.5) * self.SLOT_SIZE)
                    disk.y = self.SLOT_SIZE / DISK_DIVIDER
                    disk.display()

                # When disk is dropped.
                if disk.fall == 1:
                    self.index_of_column = int(math.floor(disk.x /
                                               self.SLOT_SIZE))
                    disk.y = disk.y + disk.SPEED

                    # makes it draw up to the slot.
                    if disk.y <= (self.SLOT_SIZE * (self.no_of_empty_slots
                                  [self.index_of_column] + 1) - (0.5)
                                  * self.SLOT_SIZE):
                        disk.display()
                    # Sets the array position to whatever player drops there.
                    else:
                        disk.y = (self.SLOT_SIZE * (self.no_of_empty_slots
                                  [self.index_of_column] + 1) - (0.5)
                                  * self.SLOT_SIZE)
                        disk.fall = 0
                        disk.settled = 1
                        self.array[self.index_of_column][
                            self.no_of_empty_slots[
                                self.index_of_column] - 1] = disk.PLAYER

                        # To prevent switching disks above full stack.
                        for disk in self.list_of_disk:
                            if disk.fall == 1:
                                self.can_go == 0
                        if self.can_go == 1:
                            # To switch players.
                            if self.player == PLAYER_ONE:
                                self.player = PLAYER_TWO
                                print("Player two's turn.")

            # the "AI".
            if disk.PLAYER == PLAYER_TWO:
                if disk.hover == 1:
                    disk.x = disk.get_x(self.array)
                    disk.y = self.SLOT_SIZE // DISK_DIVIDER
                    disk.display()

                # When disk is dropped.
                if disk.fall == 1:
                    self.index_of_column = int(math.floor(disk.x /
                                               self.SLOT_SIZE))
                    disk.y = disk.y + disk.SPEED

                    # makes it draw up to the slot.
                    if disk.y <= (self.SLOT_SIZE * (self.no_of_empty_slots
                                  [self.index_of_column] + 1) - (0.5)
                                  * self.SLOT_SIZE):
                        disk.display()
                    # Sets the array position to whatever player drops there.
                    else:
                        disk.y = (self.SLOT_SIZE * (self.no_of_empty_slots
                                  [self.index_of_column] + 1) - (0.5)
                                  * self.SLOT_SIZE)
                        disk.fall = 0
                        disk.settled = 1
                        self.array[self.index_of_column][
                            self.no_of_empty_slots[
                                self.index_of_column] - 1] = disk.PLAYER
                        # To prevent switching disks above full stack.
                        for disk in self.list_of_disk:
                            if disk.fall == 1:
                                self.can_go == 0
                        if self.can_go == 1:
                            # Reset timer and hand back to player.
                            self.timer = 0
                            self.player = 1
                            self.player_turn = True
                            print("Player one's turn.")

            # To draw the stopped disk and prevent it from
            # drawing above the board.
            if disk.settled == 1 and disk.y > self.SLOT_SIZE:
                disk.display()

            # Game over score inputs. reads and writes to score.
            if self.game_ended is True and self.input_start == 0:
                self.input_start = 1
                scores = open('scores.txt', 'r')
                lines = scores.readlines()
                score_list = []
                counter = 0

                for line in lines:
                    word = line.split()
                    if word[0] == self.name:
                        word[1] = int(word[1]) + 1
                    score_list += word
                    if word[0] != self.name:
                        counter += 1

                if counter == len(score_list)//CONST_TWO:
                    score_list.append(self.name)
                    score_list.append(self.points)

                for j in range(len(score_list)//CONST_TWO):
                    for i in range(1, len(score_list)-CONST_TWO, CONST_TWO):
                        score_list[i] = int(score_list[i])
                        if score_list[i] < int(score_list[i+CONST_TWO]):
                            score_list[i+CONST_TWO], score_list[i] = \
                                score_list[i], score_list[i+CONST_TWO]
                            score_list[i+1], score_list[i-1] = \
                                score_list[i-1], score_list[i+1]
                wr = open('scores.txt', 'w')

                for i in range(0, len(score_list)-1, CONST_TWO):
                    line = score_list[i] + ' ' + str(score_list[i+1]) + '\n'
                    wr.write(line)
