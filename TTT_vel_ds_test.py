import TTT_vel_data_structure_draft as drafty


board_in_progress_1 = {
    "key": 0,
    "state": [
        "O", "-", "-", "O",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "O", "-", "-", "O"
    ]

}

board_in_progress_2 = {
    "key": 0,
    "state": [
        "O", "-", "O", "O",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ]
}

board_in_progress_3 = {
    "key": 0,
    "state": [
        "X", "X", "X", "X",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-"
    ]
}

drafty.check_victory(board_in_progress_1, "O")
drafty.check_victory(board_in_progress_1, "X")
drafty.check_victory(board_in_progress_2, "O")
drafty.check_victory(board_in_progress_3, "X")