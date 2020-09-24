from random import choices
import copy

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

def unique_key(board, move, turn_number):
        board['key'] = str(turn_number) + "-" + str(move)
        return board

class Node():

    def __init__(self, move: int, turn_number: int, board_status, player:str, weight:float):
        self.move = move
        self.turn_number = turn_number
        self.parent = None
        self.children = []
        self.board_status = board_status
        self.player = player
        # add to aooend+child method
        self.legal_next_move = []
        self.weight = weight
        self.board_key = str(turn_number) + "-" + str(move)

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parent = self

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
                # move_arg_p = next_node.parent.move
                # next_node.parent.legal_moves(move_arg_p)
                print("Parent Legal Moves: ", next_node.parent.legal_next_move)
                print()
                for child in next_node.children:
                    print("Child Key: ", child.board_key)
                    print("Child Weight: ", child.weight)
                    print("Child Move: ", child.move)
                    # move_arg = child.move
                    # child.legal_moves(move_arg)
                    print("Child Legal Moves: ", child.legal_next_move)
                    print()
                    node_queue.append(child)
        return [i.board_status for i in visited_nodes]

    # def tree_height(self):
    #     if not self.children:
    #         return 1
    #     else:
    #         return 1 + max(child.tree_height() for child in self.children)




root = Node(0, 0, board_new, "None", 0)
# root.append_child(Node(16, 1, board_new, "X", 50.0)
# root.append_child(Node(4, 1, board_new, "X", 50.0)
# root.append_child(Node(3, 1, board_new, "X", 50.0)
# root.children[1].append_child(Node(7, 2, board_new, "O", 50.0)
# root.children[2].append_child(Node(9, 2, board_new, "O", 50.0)
# root.children[2].append_child(Node(3, 2, board_new, "O", 50.0)
# root.children[1].children[0].append_child(Node(10, 3, board_new, "X", 50.0, list(range(0,17)).remove(10)))


def tic_tac_toe(root, board):
    for index, board_space in enumerate(board_new["state"]):
       # print(index+1, board_space)
        if (index % 2) != 0 and index != 0:
            print("player X plays")
            x_move = choices(range(len(board_new["state"])), weights=[50] * len(board_new["state"]))
            x_move_int = x_move.pop()
            print(x_move_int)
            if board["state"][x_move_int] == "-":
                next_board = copy.deepcopy(board)
                unique_key(next_board, x_move_int, index)
                print(next_board["state"][x_move_int])
                next_board["state"][x_move_int] == "X"
                root.append_child(Node(x_move_int, index, next_board, "X", 50.0))
                print(next_board)
                print(root.children[0].board_status)
        elif (index % 2) == 0 and index !=0:
            print("player O plays")
            # o_move = choices(range(1, len(board_new["state"])+1), weights=[50] * len(board_new["state"]))
            # o_move_int = o_move.pop()
            # if board["state"][o_move_int] == "-":
            #     print(board["state"])
            #     next_board = copy.deepcopy(board)
            #     print(o_move_int)
            #     unique_key(next_board, o_move_int, index)
            #     next_board["state"][o_move_int] == "X"
            #     root.append_child(Node(o_move_int, index, next_board, "O", 50.0))
            #     print(next_board)



print(tic_tac_toe(root, board_new))
#print(board_new["state"].index("-"))