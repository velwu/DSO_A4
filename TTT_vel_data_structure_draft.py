# Reference: "4x4 Tic-Tac-Toe" (which has all these win conditions:
## 4-in-a-row
## holding all 4 corners
## filling any adjacent 2x2 square with your markers

# Note to self: It's Sunday so I'm cooking spaghetti codes.

import random
import copy

#TODO: Decide which data structure to use for board states.
# Board state 1: A classy class~
class TheBoard:
    def __init__(self, board_state_key):
        self.state_id = board_state_key
        self.board_state = ["-", "-", "-", "-",
                            "-", "-", "-", "-",
                            "-", "-", "-", "-",
                            "-", "-", "-", "-"]

    def set_player_move(self, player_symbol, position):
        self.board_state[position] = player_symbol

#TODO: Decide which data structure to use for board states.
# Board state 2: A dictating dictionary (currently in use)~
board_new = {
    "state": [
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

# It is assumed herein that the computer which learns plays as 'O', whereas its opponent plays 'X'
# The 'O' player is also referred to as 'learner' in some of the functions below.

def play_all_game(board):
    for each in range(0, len(board["state"])):
        if board["state"].count("X") <= board["state"].count("O"):
            print("Player X makes a move.")
            moved_board, board_before = random_move(board, "X")
        else:
            print("Player O makes a move.")
            moved_board, board_before = random_move(board, "O")
        show_me_the_board(moved_board)
        if check_victory(moved_board, "X"):
            return board
        elif check_victory(moved_board, "O"):
            return board
        board = moved_board

    print("The game concludes in a draw.")
    return board


def random_move(board, player_symbol):

    for each_index, each_value in enumerate(board["state"]):
        if each_value == "-":
            possible_outcome = copy.deepcopy(board["state"])
            possible_outcome[each_index] = player_symbol
            board["possible_outcomes"].append(possible_outcome)
    next_board = {
        "state": random.choices(
            population=board["possible_outcomes"],
            k=1
        )[0],
        "possible_outcomes": [],
        "outcome_weights": [],
        "next": None
    }
    board["next"] = next_board["state"]

    return next_board, board

def learner_move(board, player_symbol):
    #TODO: complete this function
    board["state"]
    board["outcome_weights"]
    board["next"]

    return board

def check_victory(board, player_symbol):

    # Wins by occupying 4 corners
    if player_symbol == board["state"][0] ==  board["state"][3] == board["state"][12] == board["state"][15]:
        print("Victory belongs to:", player_symbol, "who's occupied all 4 corners.")
        show_me_the_board(board)
        return True

    # Wins by taking a full row
    elif player_symbol == board["state"][0] ==  board["state"][1] == board["state"][2] == board["state"][3] or \
         player_symbol == board["state"][4] ==  board["state"][5] == board["state"][6] == board["state"][7] or \
         player_symbol == board["state"][8] ==  board["state"][9] == board["state"][10] == board["state"][11] or \
         player_symbol == board["state"][12] == board["state"][13] == board["state"][14] == board["state"][15]:
        print("Victory belongs to:", player_symbol, "who's taken a full row.")
        show_me_the_board(board)
        return True

    # Wins by taking a full column
    elif player_symbol == board["state"][0] ==  board["state"][4] == board["state"][8] == board["state"][12] or \
         player_symbol == board["state"][1] == board["state"][5] == board["state"][9] == board["state"][13] or \
         player_symbol == board["state"][2] ==  board["state"][6] == board["state"][10] == board["state"][14] or \
         player_symbol == board["state"][3] ==  board["state"][7] == board["state"][11] == board["state"][15]:
        print("Victory belongs to:", player_symbol, "who's taken a full column.")
        show_me_the_board(board)
        return True

    # Wins by taking the diagonal lines
    elif player_symbol == board["state"][0] ==  board["state"][5] == board["state"][10] == board["state"][15] or \
         player_symbol == board["state"][3] ==  board["state"][6] == board["state"][9] == board["state"][12]:
        print("Victory belongs to:", player_symbol, "who's occupied a diagonal line.")
        show_me_the_board(board)
        return True

    # Wins by taking a 2*2 square
    else:
        for i in range(0, 11):
            if player_symbol == board["state"][i] ==  board["state"][i+1] == board["state"][i+4] == board["state"][i+5]:
                print("Victory belongs to:", player_symbol, "who's occupied a 2-by-2 square.")
                show_me_the_board(board)
                return True

    return False

def show_me_the_board(board):
    iterator = 0
    for i in range(0, 4):
        print(*board["state"][iterator:iterator+4])
        iterator += 4
    print()

#The idea of recognizing rotations and optimizing them is based on this MENACE GitHub: https://github.com/mscroggs/MENACE/blob/master/menace.js
#TODO: Apply this rotation to any function that deals with boards
board_rotations =[
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],
    [12,8,4,0,13,9,5,1,14,10,6,2,15,11,7,3],
    [12,13,14,15,8,9,10,11,4,5,6,7,0,1,2,3],
    [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
    [15,11,7,3,14,10,6,2,13,9,5,1,12,8,4,0],
    [3,7,11,15,2,6,10,14,1,5,9,13,0,4,8,12],
    [3,2,1,0,7,6,5,4,11,10,9,8,15,14,13,12]
]

#TODO: Do some testing with these codes
