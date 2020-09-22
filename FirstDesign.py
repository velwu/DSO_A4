from random import choices

# board as 1D array


#TODO: Decide which data structure to use for board states.
# Board state 2: A dictating dictionary~

# this is the root
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

    def __init__(self, move: int, turn_number: int, board_status, player:str, weight:float):
        self.move = move
        self.turn_number = turn_number
        self.parent = None
        self.children = []
        self.board_status = board_status
        self.player = player
        self.legal_next_move = []
        self.weight = weight
        # self.board_key = str(board_status)

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self

    def unique_key(self, turn_number: "turn_number", move:"move"):
        self.board_status['key'] = str(turn_number) + "-" + str(move)
        return self.board_status


    def adjust_weight(self):
        # call win/loss/draw function
        # if loss:
        if self.weight > 0:
            self.weight -= 5.0
        #if win:
            #self.weight += 5.0
            return self.weight

    # can we use the board_key to get a unique id for each board? 
    # working on the tree traveresel using a queue
    def search_tree(self):
        visited_nodes = list()
        node_queue = list()
        node_queue.append(self)
       # print(node_queue[0].board_status)
        while node_queue:
            next_node = node_queue.pop()
            # print(next_node.weight)
           # print(next_node.board_status["key"])
            visited_nodes.append(next_node)
            for child in next_node.children:
                # child_unique = unique_key(child.board_status, child.move, child.turn_number)
                # child_updated = child.board_status['key']
                node_queue.append(child)
        return [i.board_status for i in visited_nodes]

    # def tree_height(self):
    #     if not self.children:
    #         return 1
    #     else:
    #         return 1 + max(child.tree_height() for child in self.children)



board_new
# print(first_board.board_state)
root = Node(0, 0, board_new, "None", 0)
root.append_child(Node(16, 1, board_new, "X", 50.0))
root.append_child(Node(4, 2, board_new, "O", 50.0))

# print(root.weight)
# print(root.board_status)
# print(root.adjust_weight())
# print(root.children[0].weight)
# print(root.children[0].adjust_weight())
# print(root.children[0].adjust_weight())
print(root.search_tree())
print(root.unique_key(4,1))
print(root.children[0].unique_key(16,2))