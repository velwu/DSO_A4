import HTL_game_rules_n_misc as game_rules_n_misc
import time
import copy
from HTL_game_rules_n_misc import create_board
"""
RUN THIS FILE USING PYCHARM OR OTHER PYTHON INTERPRETERS
Modes and what do they do:
1. "play"
- Starts a game where you the human player goes against a computer in the local console
2. "demo"
- Showcases 2 computers playing against each other in a board with width & height of your specification
3. "test"
- Runs a few test objects, and display some valid and invalid moves.
"""


game_state_example_0 = {

    "Lines": [],
    "Weights": []
}

game_state_example_1 = {
    "Lines": [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2)],
    "Weights": []
    # Without learning, the 'Weights' start out empty. Might need to loop through it to assign them.
}

game_state_example_2 = {
    "Lines": [(0, 1), (0, 2)],
    "Weights": []
}

game_state_example_3 = {
    "Lines": [(3, 3), (1, 3), (0, 2), (1, 0), (3, 1), (2, 0), (3, 0)],
    "Weights": []
}

print("Specify program type: play, test, or demo")
test_input = input()
if test_input == "test":
    # Test 0, 1, 2, 5 should pass, while 3, 4 should fail
    print("Test 0")
    test_0 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_0, "(1,1), (3,3)", 4, 4)
    print("move made:", str(test_0[1]),
          "; Current State:", test_0[0]["Lines"], "\n")

    print("Test 1")
    test_1 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_1, "(1,2),(3,1)", 4, 4)
    print("move made:", str(test_1[1]),
          "; Current State:", test_1[0]["Lines"], "\n")

    print("Test 2")
    test_2 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_1, "(0,0),(2,1)", 4, 4)
    print("move made:", str(test_2[1]),
          "; Current State:", test_2[0]["Lines"], "\n")

    print("Test 3")
    test_3 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_1, "(2,1),(3,2)", 4, 4)
    print("Current State:", game_state_example_1["Lines"], "\n")

    print("Test 4")
    test_4 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_2, "(0,2),(0,0)", 4, 4)
    print("Current State:", game_state_example_2["Lines"], "\n")

    # test_5 should pass
    print("Test 5")
    test_5 = game_rules_n_misc.make_a_move_from_input(
        game_state_example_2, "(0,2),(0,3)", 4, 4)
    print("move made:", str(test_5[1]),
          "; Current State:", test_5[0]["Lines"], "\n")

elif test_input == "play":
    # This create_board() is imported. Might need to merge these back to play_rptest.py
    try:
        custom_coords, height_limit, width_limit = create_board(int(input(
            "Enter the height of the board: ")), int(input("Enter the width of the board: ")))
    except:
        print("Unknown input format. Assuming default 4 by 4 settings.")
        custom_coords, height_limit, width_limit = create_board(4, 4)

    print("Loading game state 0")
    selected_game_state = game_state_example_0

    while True:
        player_input = input(
            'Input command: "(x1, y1),(x2,y2)"  or type Q to quit \n')
        if player_input in ['q', 'Q']:
            print("Guess we're done here. Bye!")
            break
        try:
            next_game_state = game_rules_n_misc.make_a_move_from_input(
                game_state_example_0, player_input, height_limit, width_limit)[0]
            if next_game_state == None:
                continue
        except:
            print(
                "Input format must be (x1, y1),(x2,y2) and within height/width limits. Try again!")
            continue
        selected_game_state = next_game_state
        print("Current game state:", selected_game_state["Lines"])
        if game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == True:
            print("No more potential moves left. The computer has won.")
            break
        elif game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == False:
           print("Waiting for computer's move...")
        # time.sleep(2)
        selected_game_state, coordinates = game_rules_n_misc.make_a_move_randomly(
            selected_game_state, custom_coords)
        print("Computer made a move:", coordinates)
        print("Current game state:", selected_game_state["Lines"])
        if game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == True:
            print("No more potential moves left. You have won. Congratulations!")
            break
        elif game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == False:
            print("It is now your turn.")
            continue
#make_a_move_from_input(game_state_example, "(1,2),(0,3)")

#print(intersect((0,0), (2,1), (1,1), (2,0)))\

elif test_input == "demo":
    try:
        custom_coords, height_limit, width_limit = create_board(int(input(
            "Enter the height of the board: ")), int(input("Enter the width of the board: ")))
    except:
        print("Unknown input format. Assuming default 4 by 4 settings.")
        custom_coords, height_limit, width_limit = create_board(4, 4)
    print("Loading game state 0")
    selected_game_state = game_state_example_0
    #print("Loading game state 3")
    #selected_game_state = game_state_example_3
    is_Turings_turn = -1
    # There are 2 computers: Clarke and Turing.
    # Clarke goes first and Turing goes second.
    cpu_1 = {
        "computer_name": "AI Clarke",
        "moves_made": [],
        "condition": None
    }
    move_p1 = None
    cpu_2 = {
        "computer_name": "AI Turing",
        "moves_made": [],
        "condition": None
    }
    move_p2 = None
    while True:
        if is_Turings_turn == -1:
            # time.sleep(1)
            selected_game_state, move_p1 = game_rules_n_misc.make_a_move_randomly(
                selected_game_state, custom_coords)
            cpu_1["moves_made"].append(move_p1)
            print(cpu_1["computer_name"], "made a move:", move_p1)
        if is_Turings_turn == 1:
            # time.sleep(1)
            selected_game_state, move_p2 = game_rules_n_misc.make_a_move_randomly(
                selected_game_state, custom_coords)
            cpu_2["moves_made"].append(move_p2)
            print(cpu_2["computer_name"], "made a move:", move_p2)
        print("Current game state:", selected_game_state["Lines"])
        if game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == False:
            is_Turings_turn *= -1
            continue
        elif game_rules_n_misc.is_game_over(selected_game_state, custom_coords)[0] == True:
            print("The game concludes.")
            print("Final game state:", selected_game_state["Lines"])

            if is_Turings_turn == -1:
                cpu_1["condition"] = "Loss"
                cpu_2["condition"] = "Win"
                print(cpu_2["computer_name"], "Wins")
            elif is_Turings_turn == 1:
                cpu_1["condition"] = "Win"
                cpu_2["condition"] = "Loss"
                print(cpu_1["computer_name"], "Wins")

            print(cpu_1["computer_name"], "'s moves:", cpu_1["moves_made"])
            print(cpu_2["computer_name"], "'s moves:", cpu_2["moves_made"])
            break

else:
    print("COMMAND NOT RECOGNIZED. SHUTTING DOWN.")