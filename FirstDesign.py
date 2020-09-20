# board as 1D array


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
    # travel back up the tree
    print("new move")

# Maybe should a class?
def matchboxes():
    matchbox = list()
    bead = str
    # keep track of failures and success
    # get rid of the failures and keep success
    print("learning with matchboxes")

def output():
    # number of games run and loss and wins?
    print("Finished Game")
