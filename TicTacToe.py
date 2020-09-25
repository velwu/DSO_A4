

# Note: This is the place where the main codes are replicated such that methods which export learning outcomes to a pickle file could be experimented with.

# The outcome of this experiment is included in the main file.

import pickle
import random


board_new = [
    "-", "-", "-", "-",
    "-", "-", "-", "-",
    "-", "-", "-", "-",
    "-", "-", "-", "-"
]

# It is assumed herein that the computer which learns plays as 'O', whereas its opponent plays 'X'
# The 'O' player is also referred to as 'learner' in some of the functions below.


def play_all_game(board):
    result = "Draw"

    temp_memory = {}
    for each in range(0, len(board)):
        if board.count("X") <= board.count("O"):
            moved_board, board_before = random_move(board, "X")
        else:
            moved_board, board_before = learner_move(board, "O")

        show_me_the_board(moved_board)
        if check_victory(moved_board, "X"):
            result = "Loss"
            adjust_weights("Loss")

            return result
        elif check_victory(moved_board, "O"):
            adjust_weights("Win")
            result = "Win"
            return result
        board = moved_board

    adjust_weights("Draw")
    # result="Draw"
    return result


def adjust_weights(state):
    print(state)
    if state == "Win":
        for key, value in temp_memory.items():
            game_memory[str(key)][value] += 10
    elif state == "Loss":
        for key, value in temp_memory.items():
            game_memory[str(key)][value] -= 10
    elif state == "Draw":
        for key, value in temp_memory.items():
            game_memory[str(key)][value] += 10

    return None


def possible_moves(board):
    p_moves = board.count('-')
    p_indices = []
    for i in range(16):
        if board[i] == '-':
            p_indices.append(i)
    return p_moves, p_indices


def random_move(board, player_symbol):
    previous_board = board
    moves, indices = possible_moves(board)
    fetch_indices = random.choice(indices)
    board[fetch_indices] = player_symbol
    return board, previous_board


def temp_insert_state(board, index):
    temp_memory[''.join(board)] = index


def game_insert_state(board, moves, indices):
    #  print(board, moves, indices, "Insert Game Mem")
    temp_dict = {}
    for i in range(0, moves):
        temp_dict[indices[i]] = 100

    game_memory[''.join(board)] = temp_dict


def learner_move(board, player_symbol):
    moves, indices = possible_moves(board)
    previous_board = board
    if ''.join(board) in game_memory:
        #   print("New Pattern")
        fetch_indices = random.choices(list(game_memory[''.join(board)].keys()),
                                       weights=game_memory[''.join(board)].values(), k=1)

    else:

        show_me_the_board(board)
        game_insert_state(board, moves, indices)
        # list(game_memory[''.join(board)].values())
        fetch_indices = random.choices(list(game_memory[''.join(board)].keys()),
                                       weights=list(game_memory[''.join(board)].values()), k=1)

    show_me_the_board(board)
    # print("Pattern -", ''.join(board) , "Picked weight of the item Picked - ",game_memory[''.join(board)][fetch_indices[0]], fetch_indices)
    temp_insert_state(board, fetch_indices[0])

    board[fetch_indices[0]] = player_symbol

    return board, previous_board


def check_victory(board, player_symbol):
    # Wins by occupying 4 corners
    if player_symbol == board[0] == board[3] == board[12] == board[15]:
        print("Victory belongs to:", player_symbol, "who's occupied all 4 corners.")
        show_me_the_board(board)
        return True

    # Wins by taking a full row
    elif player_symbol == board[0] == board[1] == board[2] == board[3] or \
            player_symbol == board[4] == board[5] == board[6] == board[7] or \
            player_symbol == board[8] == board[9] == board[10] == board[11] or \
            player_symbol == board[12] == board[13] == board[14] == board[15]:
        print("Victory belongs to:", player_symbol, "who's taken a full row.")
        show_me_the_board(board)
        return True

    # Wins by taking a full column
    elif player_symbol == board[0] == board[4] == board[8] == board[12] or \
            player_symbol == board[1] == board[5] == board[9] == board[13] or \
            player_symbol == board[2] == board[6] == board[10] == board[14] or \
            player_symbol == board[3] == board[7] == board[11] == board[15]:
        print("Victory belongs to:", player_symbol, "who's taken a full column.")
        show_me_the_board(board)
        return True

    # Wins by taking the diagonal lines
    elif player_symbol == board[0] == board[5] == board[10] == board[15] or \
            player_symbol == board[3] == board[6] == board[9] == board[12]:
        print("Victory belongs to:", player_symbol, "who's occupied a diagonal line.")
        show_me_the_board(board)
        return True

    # Wins by taking a 2*2 square
    else:
        for i in range(0, 11):
            if player_symbol == board[i] == board[i + 1] == board[i + 4] == board[i + 5]:
                print("Victory belongs to:", player_symbol, "who's occupied a 2-by-2 square.")
                show_me_the_board(board)
                return True

    return False


def show_me_the_board(board):
    iterator = 0
    for i in range(0, 4):
        print(*board[iterator:iterator + 4])
        iterator += 4
    print()


def Simulator(number):
    print("Running Simulations for ", number, " Games")

    Random_X = 0
    Learner_O = 0
    Drawn = 0

    for i in range(0, number):
        #  print("iteration - ",i)
        board_new = [
            "-", "-", "-", "-",
            "-", "-", "-", "-",
            "-", "-", "-", "-",
            "-", "-", "-", "-"
        ]
        #   print(board_new)
        res = play_all_game(board_new)
        #  print("Result - ",res)
        if res == "Draw":
            Drawn += 1
        elif res == "Win":
            Learner_O += 1
        elif res == "Loss":
            Random_X += 1

    # print(json.dumps(game_memory, indent=2), "JSON Dumps!")
    print("Summary - ")
    print("Wins - ", Learner_O, "Losses - ", Random_X, "Draws - ", Drawn)


# The idea of recognizing rotations and optimizing them is based on this MENACE GitHub: https://github.com/mscroggs/MENACE/blob/master/menace.js
# TODO: Apply this rotation to any function that deals with boards
board_rotations = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15],
    [12, 8, 4, 0, 13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3],
    [12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3],
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [15, 11, 7, 3, 14, 10, 6, 2, 13, 9, 5, 1, 12, 8, 4, 0],
    [3, 7, 11, 15, 2, 6, 10, 14, 1, 5, 9, 13, 0, 4, 8, 12],
    [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12]
]

# play_all_game(board_new)

# with open('data.p', 'rb') as fp:
#    game_memory = pickle.load(fp)
game_memory = {}

temp_memory = {}

try:
    game_memory = pickle.load(open("Game_Memory.pickle", "rb"))
except (OSError, IOError) as e:
    pickle.dump(game_memory, open("Game_Memory.pickle", "wb"))

Simulator(100)

with open('Game_Memory.pickle', 'wb') as fp:
    pickle.dump(game_memory, fp, protocol=pickle.HIGHEST_PROTOCOL)

# print("##################################################")
# print("################    GAME      ####################")
# print("##################################################")
#
#
# print(json.dumps(game_memory, indent=2), "JSON Dumps!")
# print("##################################################")
# print("################    TEMP      ####################")
# print("##################################################")
#
# print(json.dumps(temp_memory, indent=2), "JSON Dumps!")

# TODO: Do
