'''
 A main file for running the board game with human player
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''

from time import time_ns
from PlayBoardGame import PlayBoardGame

for depth in range(5, 8):
    for size in range(5, 8):
        for answer in ['Simple', 'Smart']:
            start = time_ns()
            answer = answer.lower()
            # create a game playing object
            game = PlayBoardGame(size, depth, answer)

            # allow person to select starter
            game.select_starter()

            # as long as not finished
            while not(game.finished()):
                # brint game board and other information
                game.print_status()

                # allow the player in turn to move, either human or computer
                game.select_move()

            print(f"time ms: {round((time_ns()-start)/(10**6), 2)} \
                \nplayers: {answer}\
                \nsize of the board:{size}\
                \ndepth of search:{depth}")