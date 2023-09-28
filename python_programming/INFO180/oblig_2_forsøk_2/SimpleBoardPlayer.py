'''
Class that represent the features and methods for a Simple Computer Board game player
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''


from Board import CROSS, RING
from BoardComputerPlayer import BoardComputerPlayer


class SimpleBoardPlayer(BoardComputerPlayer):

    def __init__(self, the_mark, size, depth):
        '''
        Constructor
        :param compatibility_score_set:
        '''
        super(SimpleBoardPlayer, self).__init__(the_mark, depth)
        self.name = "Simple"
        self.size = size

    def evaluate_game_status(self, a_board):
        max_cross_row = 0
        max_ring_row = self.size-1
        for i in range(self.size):
            for j in range(self.size):
                if a_board.the_grid[i][j] == CROSS:
                    if i > max_cross_row:
                        max_cross_row = i
                if a_board.the_grid[i][j] == RING:
                    if i < max_ring_row:
                        max_ring_row = i
        score = 0
        if self.mark == CROSS:
            score = max_cross_row - (self.size-1-max_ring_row)
        if self.mark == RING:
            score = (self.size-1-max_ring_row) - max_cross_row
        return score

class SmartBoardPlayer(BoardComputerPlayer):

    def __init__(self, the_mark, size, depth):
        '''
        Constructor
        :param compatibility_score_set:
        '''
        super(SmartBoardPlayer, self).__init__(the_mark, depth)
        self.name = "Simple"
        self.size = size

    def evaluate_game_status(self, a_board):
        max_cross_row = 0 
        max_ring_row = self.size-1

        for i in range(self.size):
            for j in range(self.size):
                if a_board.the_grid[i][j] == CROSS:
                    if max_cross_row == 0:
                        max_cross_row = i
                        break
            if max_cross_row != 0:
                break

        for i in range(self.size-1, 0, -1):
            for j in range(self.size-1, 0, -1):
                if a_board.the_grid[i][j] == RING:
                    if max_ring_row == self.size-1:
                        max_ring_row = i
                        break
            if max_ring_row != self.size-1:
                break

        score = 0
        if self.mark == CROSS:
            score = max_cross_row - (self.size-1-max_ring_row)
        if self.mark == RING:
            score = (self.size-1-max_ring_row) - max_cross_row
        return score


