## create tree
## create infinite nodes in tree

# create class for each node in the tree, not whole tree
# all trees are graphs, no loops (can't be cyclical), directed, top down
# can typicallly apply graph functionality to a tree
# game tree - start move - how many legal turns does player one have? Each move creates a "game state" (what is on the board and where, and any off board counters, score, what turn is it, who turn is it next, ), 
# memory saving - traverse up the tree and only store latest move, or store x and y coords in tuple as a dict key and maintain list values

# homework re-create matchbox tictactoe with randomly generated moves (with custom weighting, depending on each number of colored beads), also store each legal, possible moves

# simulating random choices with weights
from random import choices

# for x in range(10):
#     print(choices(['red', 'blue', 'green'], weights=[1, 1, 3]))

class GameState:
    
    def __init__(self, board_status, turn_number, player):
        self.board_status = board_status
        self.turn_number = turn_number
        self.player = player
        self.legal_next_move = []

class Node:

    def __init__(self, move: int, game_state = 'GameState'):
        self.move = move
        self.game_state = game_state
        self.parent = None
        self.children = []
        
    def append_child(self, child: 'Node'):
        self.children.append(child)
        child.parent = self


x = Node(5, "X")

x.append_child(Node(2))
x.append_child(Node(3))

x.children[1].append_child(Node(82))

for i in x.children:
    print(i.parent.move)


