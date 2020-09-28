import random
import copy
import numpy as np
import copy
import json
from os import error
from datetime import datetime

empty_board_numpy = np.array([
])

# one line drawn by any player is represented as: [(0,0), (0,1), (0,2), (0,3)], [(2,0), (2,1), (2,2), (2,3)], etc.

#TODO: Build a game rule on this data structure:
# It is assumed that everything in the game_state is a legal move
game_state_example = {"PlayerA" : [[(0,0), (0,1), (0,2), (0,3)], [(2,0), (2,1), (2,2), (2,3)]],
                      "PlayerB" : [[(1,0), (1,1), (1,2), (1,3)], [(3,0), (3,1), (3,2), (3,3)]]
              }

empty_board = [["-", "-", "-", "-"],
               ["-", "-", "-", "-"],
               ["-", "-", "-", "-"],
               ["-", "-", "-", "-"]]

def visualize_game(board, game_state):
    for each_row in game_state["PlayerA"]:
        for each_col_value in each_row:
            board[each_col_value[0]][each_col_value[1]] = "A"
    for each_row in game_state["PlayerB"]:
        for each_col_value in each_row:
            board[each_col_value[0]][each_col_value[1]] = "B"
    iterator = 0
    for i in range(0, len(board)):
        print(*board[iterator])
        iterator += 1

visualize_game(empty_board, game_state_example)