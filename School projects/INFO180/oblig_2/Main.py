'''
 A main file for running the board game with human player
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''

from time import time_ns
from PlayBoardGame import PlayBoardGame

for i in range(5, 8):
    for j in range(5, 8):
        for answer in ['simple', 'smart']:
            # create a game playing object
            game = PlayBoardGame(answer[:4], i, j)

            # allow person to select starter
            game.select_starter()

            start_time = time_ns()

            # as long as not finished
            while not(game.finished()):
                # brint game board and other information
                game.print_status()

                # allow the player in turn to move, either human or computer
                game.select_move()

            print(f'time : {round((time_ns()-start_time)/(10**6), 0)} ms \n\
players = "{answer}" \n\
size = {i} \n\
depth = {j}')
            game.print_result()