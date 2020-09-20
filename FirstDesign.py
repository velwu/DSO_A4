# board as 1D array
# board as dict?

board = {}

for i in range(1, 17):
    if i not in board:
        board[i] = ""
print(board)

for tile in range(len(board)):
    tile =


class Tile:

    def __init__(self, position, move):
        self.position =position
        self.move = move

class GameState:

    def __init__(self, board_status, turn_number, player):
        self.board_status = board_status
        self.turn_number = turn_number
        self.player = player
        self.legal_next_move = []

class Node:

    def __init__(self, move: int, game_state='GameState'):
        self.move = move
        self.game_state = game_state
        self.parent = None
        self.children = []

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self


def final_move():
    # conditions for a win, draw, and loss
    # if there are no consecutive spaces left
    print("game over")

def validate_moves():
    # make sure the move is possible
    # is that board not full?
    # that local spot taken?
    print("validate")

def generate_next_move():
    # keep track of last move
    print("new move")

def matchboxes():
    matchbox = list()
    bead = str
    print("learning with matchboxes")

def output():
    print("Finished Game")
