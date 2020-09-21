from random import choices

# board as 1D array


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


class Node():

    def __init__(self, move: int, board_status, player:str, weight:float):
        self.move = move
        self.parent = None
        self.children = []
        self.board_status = board_status
        self.player = player
        self.legal_next_move = []
        self.weight = weight

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self

    def adjust_weight(self):
        if self.weight > 0:
            self.weight -= 5.0
            return self.weight

    # working on the tree travesl using a queue
    def search_tree(self, root):
        visited_nodes = list()
        node_queue = list()
        while node_queue:
            next_node = node_queue.pop()
            visited_nodes.append(next_node)
            for child in self.children:
                node_queue.append(child)   

    def tree_height(self):
        if not self.children:
            return 1
        else:
            return 1 + max(child.tree_height() for child in self.children)



first_board = board_new
# print(first_board.board_state)
root = Node(1, first_board, "X", 50.0)
root.append_child(Node(2, first_board, "O", 50.0))

print(root.weight)
print(root.board_status)
print(root.adjust_weight())
print(root.children[0].weight)
print(root.children[0].adjust_weight())
print(root.children[0].adjust_weight())
