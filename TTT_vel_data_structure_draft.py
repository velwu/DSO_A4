# Reference: "4x4 Tic-Tac-Toe" (which has all these win conditions:
## 4-in-a-row
## holding all 4 corners
## filling any adjacent 2x2 square with your markers

# Note to self: It's Sunday so I'm cooking spaghetti codes.

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
# Board state 2: A dictating dictionary~
board_new = {
    "key": 0,
    "state": [
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ]
}

def check_victory(board, player_symbol):
    if player_symbol == board["state"][0]:
        if board["state"][0] ==  board["state"][3] == board["state"][12] == board["state"][15]:
            print("Victory belongs to:", player_symbol)
            show_me_the_board(board)
            return True
        elif board["state"][0] ==  board["state"][1] == board["state"][2] == board["state"][3]:
            print("Victory belongs to:", player_symbol)
            show_me_the_board(board)
            return True
        else:
            print("nothing is happening for", player_symbol)
            show_me_the_board(board)
            return False
    else:
        print("nothing is happening for", player_symbol)
        show_me_the_board(board)
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
