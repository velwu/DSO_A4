import TTT_vel_rajath_samantha as TTT_solution
import pickle

board_new = {
    "state": [
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

learned_boards = [
    {"value": [
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ],
        "weight": 50},

    {"value": [
        "O", "-", "O", "O",
        "-", "X", "-", "-",
        "-", "X", "-", "-",
        "-", "-", "-", "-"
    ],
        "weight": 100},

    {"value": [
        "X", "X", "X", "X",
        "-", "O", "-", "O",
        "-", "O", "-", "-",
        "O", "-", "O", "-"
    ],
        "weight": 10}

    # random.choices(weight=)
]

empty_board = {
    "state": [
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

board_in_progress_1 = {
    "state": [
        "O", "-", "-", "O",
        "-", "X", "X", "-",
        "-", "X", "-", "-",
        "O", "-", "-", "O"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

board_in_progress_2 = {
    "state": [
        "O", "-", "O", "O",
        "-", "X", "-", "-",
        "-", "X", "-", "-",
        "-", "-", "-", "-"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

board_in_progress_3 = {
    "state": [
        "X", "X", "X", "X",
        "-", "O", "-", "O",
        "-", "O", "-", "-",
        "O", "-", "O", "-"
    ],
    "possible_outcomes": [],
    "outcome_weights": [],
    "next": None
}

#TTT_solution.play_games_record_them(empty_board, True, 1000, True, 100)

try:
    game_memory = pickle.load(open("Game_Memory.pickle", "rb"))
except (OSError, IOError) as e:
    pickle.dump(game_memory, open("Game_Memory.pickle", "wb"))

TTT_solution.play_games_record_them(empty_board, True, 1000000, True, 10000)

with open('Game_Memory.pickle', 'wb') as fp:
    pickle.dump(game_memory, fp, protocol=pickle.HIGHEST_PROTOCOL)

#for i in range(0, 100):
#    drafty.play_all_game(empty_board, True)