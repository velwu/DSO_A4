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
game_state_example_1 = {"Lines" : [(0,0), (0,1), (0,2), (0,3), (1,2)]
              }
game_state_example_2 = {"Lines" : []}

def visualize_game(game_state):
    board_for_printing = [["-", "-", "-", "-"],
                          ["-", "-", "-", "-"],
                          ["-", "-", "-", "-"],
                          ["-", "-", "-", "-"]]
    for each_col_value in game_state["Lines"]:
        board_for_printing[each_col_value[0]][each_col_value[1]] = "*"
    iterator = 0
    for i in range(0, len(board_for_printing)):
        print(*board_for_printing[iterator])
        iterator += 1

def make_a_move_from_input(game_state, move_syntax):
    move_parsed = eval(move_syntax)
    for each in enumerate(move_parsed):
        print(each[1])
        if each[1] not in game_state["Lines"]:
            game_state["Lines"].append(each[1])
    print(game_state)
    visualize_game(game_state)

#visualize_game(game_state_example_1)
make_a_move_from_input(game_state_example_2, "(0,0),(2,1)")
