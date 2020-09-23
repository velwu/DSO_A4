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


Player_O_wins = 0
Player_O_loses = 0
ADraw = 0


def output(wins, loses, adraw):
    # number of games run and loss and wins?
    # if a win:
    wins += 1
    # if a loss
    loses += 1
    # if a draw
    adraw += 1
    print("Finished Game")



class Node():

    def __init__(self, move: int, turn_number: int, board_status, player:str, weight:float, legal_next_move: list):
        self.move = move
        self.turn_number = turn_number
        self.parent = None
        self.children = []
        self.board_status = board_status
        self.player = player
        # add to aooend+child method
        self.legal_next_move = legal_next_move
        self.weight = weight
        self.board_key = str(turn_number) + "-" + str(move)

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self

    def unique_key(self):
        self.board_status['key'] += str(self.turn_number) + "-" + str(self.move)
        #return self.board_status

    def legal_moves(self, move):
        self.legal_next_move = list(range(0, 17))
        self.legal_next_move.remove(move)
        #print(node.legal_next_move.remove(move) for node in self.search_tree())
        return self.legal_next_move


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
            visited_nodes.append(next_node)
            if  next_node.parent != None:
                print()
                print("Parent Key: ", next_node.parent.board_key)
                print("Parent Weight: ", next_node.parent.weight)
                print("Parent Move: ", next_node.parent.move)
                print("Parent Legal Moves: ", next_node.parent.legal_next_move)
                print()
                for child in next_node.children:
                    print("Child Key: ", child.board_key)
                    print("Child Weight: ", child.weight)
                    print("Child Move: ", child.move)
                    print("Child Legal Moves: ", child.legal_next_move)
                    print()
                    node_queue.append(child)
        return [i.board_status for i in visited_nodes]

    # def tree_height(self):
    #     if not self.children:
    #         return 1
    #     else:
    #         return 1 + max(child.tree_height() for child in self.children)




root = Node(0, 0, board_new, "None", 0, list(range(0,17)))
root.append_child(Node(16, 1, board_new, "X", 50.0, list(range(0,17)).remove(16)))
root.append_child(Node(4, 1, board_new, "X", 50.0, list(range(0,17)).remove(4)))
root.append_child(Node(3, 1, board_new, "X", 50.0, list(range(0,17)).remove(3)))
root.children[1].append_child(Node(7, 2, board_new, "O", 50.0, list(range(0,17)).remove(7)))
root.children[2].append_child(Node(9, 2, board_new, "O", 50.0, list(range(0,17)).remove(9)))
root.children[2].append_child(Node(3, 2, board_new, "O", 50.0, list(range(0,17)).remove(3)))
root.children[1].children[0].append_child(Node(10, 3, board_new, "X", 50.0, list(range(0,17)).remove(10)))

# print(root.weight)
# print(root.board_status)
# print(root.adjust_weight())
# print(root.children[0].weight)
# print(root.children[0].adjust_weight())
# print(root.children[0].adjust_weight())
#print(root.children[1].children[0].search_tree())
# print(root.children[1].children[0].search_tree())
# print(root.unique_key(4,1))
# print(root.children[0].unique_key(16,2))
print("Legal Moves: ", root.children[1].legal_moves(4))
#print("Legal Moves: ", root.children[1].children[0].legal_moves(8))