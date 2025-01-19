'''
 Program that allows a human player to play against a simple computer player of a simple board game
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''
from Board import Board, NOT_TERMINAL, CROSS, RING
from BoardHumanPlayer import BoardHumanPlayer
from SimpleBoardPlayer import SimpleBoardPlayer, SmartBoardPlayer


class PlayBoardGame:
    '''
    The class that controls the play of the board game
    '''

    def __init__(self, size:int = 5, depth:int = 5, answer:str = 'simp'):
        '''
        Initialise the game
        '''
        self.player1 = None
        self.player2 = None
        self.game_board = Board(size=size)
        self.to_move = None
        self.status = NOT_TERMINAL
        self.size = size
        self.depth = depth
        self.answer = answer

    def select_starter(self):
        '''
        Asking the human player who shall start
        sets the players, their marks, and who is to move
        :return: nothing
        '''
        while self.to_move is None:
            if self.answer == "simple":
                self.player1 = SimpleBoardPlayer(CROSS, self.size, self.depth)
                self.player2 = SimpleBoardPlayer(RING, self.size, self.depth)
                self.to_move = self.player1
                self.other = self.player2

            if self.answer == "smart":
                self.player1 = SmartBoardPlayer(RING, self.size, self.depth)
                self.player2 = SmartBoardPlayer(CROSS, self.size, self.depth)
                self.to_move = self.player2
                self.other = self.player1

    def select_move(self):
        '''
        Allowing the one who is to move to do the actual move
        :return:
        '''
        moves = self.game_board.check_and_generate_moves()
        if self.game_board.game_status == NOT_TERMINAL:
            # only move if not finished
            self.game_board = self.to_move.move(self.game_board,moves)
            self.to_move, self.other = self.other, self.to_move
        else:
            # otherwise set the status of the game to status of the board
            self.status = self.game_board.game_status

    def finished(self):
        '''
        Is game finished
        :return:
        '''
        return self.status != NOT_TERMINAL

    def print_result(self):
        '''
        Prints the final result of the game
        :return:
        '''
        if self.status == CROSS and self.player2.mark == CROSS:
            print(self.player2.name + " WON! ")
        elif self.status == CROSS and self.player1.mark == CROSS:
            print(self.player1.name + " WON! ")
        elif self.status == RING and self.player2.mark == RING:
            print(self.player2.name + " WON! ")
        elif self.status == RING and self.player1.mark == RING:
            print(self.player1.name + " WON! ")
        else:
            print("DRAW")

    def print_status(self):
        '''
        Prints status of the game
        :return:
        '''
        print(self.game_board)

