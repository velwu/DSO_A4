from random import choices

# board as 1D array

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


# class GameState:
#
#     def __init__(self, board_status, turn_number, player):
#         self.board_status = board_status
#         self.turn_number = turn_number
#         self.player = player
#         self.legal_next_move = []
#
# class Node(GameState):
#
#     def __init__(self, move: int, game_state="GameState"):
#         super().__init__(self)
#         self.move = move
#         self.game_state = game_state
#         self.parent = None
#         self.children = []
#
#     def append_child(self, child: "Node"):
#         self.children.append(child)
#         child.parent = self
#
# first_board = TheBoard(0)
# # print(first_board.board_state)
# test = Node(1)
# print(test.player)

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

# we also need  a way to track duplicate situations

def matchboxes():
    matchbox = list()
    bead = str
    # keep track of failures and success
    # get rid of the failures and keep success
    print("learning with matchboxes")

def output():
    # number of games run and loss and wins?
    print("Finished Game")

def random_player(board):
    for x in range(1,17):
        print(x)
        choice = choices(['X', 'O'])
        board.set_player_move(choice, x)
        return board



class Node():

    def __init__(self, move: int, board_status, turn_number:int, player:str, game_state="game_state",):
        self.move = move
        self.game_state = game_state
        self.parent = None
        self.children = []
        self.board_status = board_status
        self.turn_number = turn_number
        self.player = player
        self.legal_next_move = []

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self

    def tree_height(self):
        if not self.children:
            return 1
        else:
            return 1 + max(child.tree_height() for child in self.children)



first_board = TheBoard(0)
# print(first_board.board_state)
test1 = Node(1, first_board, 1, "X")
print(test1.board_status.board_state)
test1.append_child(Node(2, first_board, 2, "O"))
test1.append_child(Node(3, first_board, 3, "X"))
test1.children[1].append_child(Node(3, first_board, 2, "O"))
print(test1.children[0].move)

print(test1.tree_height())

