import TTT_vel_data_structure_draft as drafty

#TODO: Remove the possible_outcomes attribute. They should be referenced in a global space.

# Board state 2: A dictating dictionary (currently in use)~
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

#drafty.check_victory(board_in_progress_1, "O")
#drafty.check_victory(board_in_progress_1, "X")
#drafty.check_victory(board_in_progress_2, "O")
#drafty.check_victory(board_in_progress_3, "X")


#board_after_1, board_before_1 = drafty.random_move(board_in_progress_1, "X")
#print(board_before_the_move)
#drafty.show_me_the_board(board_before_1)
#drafty.show_me_the_board(board_after_1)
#board_after_2, board_before_2 = drafty.random_move(board_after_1, "O")
#drafty.show_me_the_board(board_before_2)
#drafty.show_me_the_board(board_after_2)

#board_after_3, board_before_3 = drafty.random_move(board_after_2, "X")
#drafty.show_me_the_board(board_before_3)
#print("POSSIBLE OUTCOMES", *board_before_3["possible_outcomes"])

drafty.play_all_game(empty_board)
