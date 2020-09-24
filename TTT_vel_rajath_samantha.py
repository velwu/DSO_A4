"""
# Team members: (Name / GitHub ID / NetID)

Samantha Walkow / samwalkow / ??

Rajath John / jrajath94 / ??

Vel (Tien-Yun) Wu / velwu / tienyun2

"""


# Choice of topic: "4x4 Tic-Tac-Toe" (which has all these win conditions:
## 4-in-a-row
## holding all 4 corners
## filling any adjacent 2x2 square with your markers
import random
import copy
from datetime import datetime
#import FirstDesign as FD

# It is assumed herein that the machine which learns always plays as 'O', whereas its opponent plays 'X'
# The 'O' player is also referred to as 'learner' in some of the functions below.

# Tree or hashmap?: learned_board_repository - gets kept til the end of time
learned_board_repository = {}

"""
{"XX--OO--XO-X----" : 70.0, 
"XX--OO--XO-X---O": 50.0, 
"XX--OO--XO-XX--O": 20.0}
"""
# Tree 2?: current_game_moves - gets wiped/reset every time a new game starts. It's there for branching decision nodes

#TODO: 1. Make both players learn (currently only "O" is learning)
#TODO: 2. Export the learned data to an external file that can be imported

def play_games_record_them(board, learning, how_many_rounds, resetting_scores, reset_interval):
    # Obviously, reset_interval should be smaller than how_many_rounds

    if resetting_scores:
        score_board_for_Player_O = {"Win": 0, "Loss": 0, "Draw": 0}
        scored_games_count = 0
        for each in range(0, how_many_rounds):
            game_result = play_a_game(board, learning, False)
            score_board_for_Player_O[game_result] += 1
            scored_games_count += 1
            print(score_board_for_Player_O)

            if scored_games_count == reset_interval:
                #print(score_board_for_Player_O)
                with open("records.txt", "a") as file_object:
                    file_object.write(str(score_board_for_Player_O) + " " + datetime.now().strftime("%H:%M:%S") + "\n")
                scored_games_count = 0
                score_board_for_Player_O = {"Win": 0, "Loss": 0, "Draw": 0}

    else:
        score_board_for_Player_O = {"Win" : 0, "Loss" : 0, "Draw" : 0}
        for each in range(0, how_many_rounds):
             game_result = play_a_game(board, learning, False)
             score_board_for_Player_O[game_result] += 1
             #print(score_board_for_Player_O)

        print(score_board_for_Player_O)


def play_a_game(board, learning, show_each_move):
    current_game_moves = []
    for each in range(0, len(board["state"])):
        if board["state"].count("X") <= board["state"].count("O"):
            #print("Player X makes a move.")
            moved_board, board_before = random_move(board, "X")
        elif learning == True:
            #print("Player O makes a move.")
            moved_board, board_before, chosen_move = learner_move(board, "O")
            current_game_moves.append(chosen_move)
        elif learning == False:
            #print("Player O makes a move.")
            moved_board, board_before = random_move(board, "O")
        if show_each_move:
            show_me_the_board(moved_board)


        if check_victory(moved_board, "X"):
        # if "X" wins (means this is a loss for "O")
            # loop through all games moves taken
            for each in current_game_moves:
                # punish a move if it is already known/learned and not zero
                if each in learned_board_repository:
                    if learned_board_repository[each] > 0:
                        learned_board_repository[each] -= 5
                else:
                    learned_board_repository[each] = 45
            print(len(learned_board_repository), "learned moves:")
            #return board, "Loss"
            return "Loss"
        elif check_victory(moved_board, "O"):
        #if "O" wins, all moves made in this game might deserve rewards
            # loop through all games moves taken
            
            for each in current_game_moves:
                # reward  a move if it is already known/learned
                if each in learned_board_repository:
                    learned_board_repository[each] += 5
                else:
                    learned_board_repository[each] = 55
            print(len(learned_board_repository), "learned moves:")
            #return board, "Win"
            return "Win"
        board = moved_board

    # if this following section is reached at all, it means that all cells have been filled without any checks above passing
    # that is, the game is a draw.
    # loop through all games moves taken
    for each in current_game_moves:
        # only record previously unknown moves
        if each not in learned_board_repository:
            learned_board_repository[each] = 50
    print("The game concludes in a draw.")
    print(len(learned_board_repository), "learned moves:")
    #return board, "Draw"
    show_me_the_board(board)
    return "Draw"


def random_move(board, player_symbol):

    for each_index, each_value in enumerate(board["state"]):
        if each_value == "-":
            possible_outcome = copy.deepcopy(board["state"])
            possible_outcome[each_index] = player_symbol
            board["possible_outcomes"].append("".join(possible_outcome))
    next_board = {
        "state": list(random.choices(
            population=board["possible_outcomes"],
            k=1
        )[0]),
        "possible_outcomes": [],
        "outcome_weights": [],
        "next": None
    }
    board["next"] = next_board["state"]

    return next_board, board


def learner_move(board, player_symbol):
    for each_index, each_value in enumerate(board["state"]):
        if each_value == "-":
            possible_outcome = copy.deepcopy(board["state"])
            possible_outcome[each_index] = player_symbol
            board["possible_outcomes"].append("".join(possible_outcome))
            board["outcome_weights"].append(50)

    for each_idx, each_val in enumerate(board["possible_outcomes"]):
        if each_val in learned_board_repository:
            #if one of the possible legal outcomes from the current board is already learned with weights in the repo
            #board["possible_outcomes"].append(each) #add the previously learned board state to currently possible moves (key in hashmap)
            board["outcome_weights"][each_idx] = learned_board_repository[each_val] #add the weight (value in hashmap)

            #since randomly generated moves only have weights of 1.0, any learned moves should be heavily preferred unless punished into oblivion (weight = 0)
    """
    if a_node in learned_board_repository:
        next_board = a_node["state"]
        random.choices()
    if a_node not in learned_board_repository:
        a_node = Node("".join(next_board["state"]), player_symbol, 50.0)
        learned_board_repository.append(a_node)     
    """
    chosen_move = random.choices(population=board["possible_outcomes"],weights=board["outcome_weights"],k=1)[0]

    next_board = {
        "state": list(chosen_move),
        "possible_outcomes": [],
        "outcome_weights": [],
        "next": None
    }
    board["next"] = next_board["state"]

    return next_board, board, chosen_move

def contains(list, filter):
    # https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python
    # This reference was necessary for finding a class instance in the global space where the learned board states with their weights are stored.
    for x in list:
        if filter(x):
            return True
    return False



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
        for i in [0, 1, 2, 4, 5, 6, 8, 9, 10]:
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
#TODO: We thought about the possibilities of rotations, but then decided to ignore the issue in favor of simpler codes.
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
