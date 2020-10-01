import HTL_game_rules_n_misc as game_rules_n_misc

"""
TEST CODES BELOW:
"""


game_state_example_0 = {
    "Lines": [],
    "Weights": []
}

game_state_example_1 = {
    "Lines": [(0,0), (0,1), (0,2), (0,3), (1,2)],
    "Weights": []
    # Without learning, the 'Weights' start out empty. Might need to loop through it to assign them.
}

game_state_example_2 = {
    "Lines": [(0,1), (0,2)],
    "Weights": []
}

print("Specify program type: play or demo")
test_input = input()
if test_input == "demo":
    # Test 0, 1, 2, 5 should pass, while 3 and 4 should fail
    print("Test 0")
    test_0 = game_rules_n_misc.make_a_move_from_input(game_state_example_0, "(1,1), (4,4)")
    print("move made:", str(test_0[1]), "; Current State:",test_0[0]["Lines"], "\n")

    print("Test 1")
    test_1 = game_rules_n_misc.make_a_move_from_input(game_state_example_1, "(1,2),(3,1)")
    print("move made:", str(test_1[1]), "; Current State:",test_1[0]["Lines"], "\n")

    print("Test 2")
    test_2 = game_rules_n_misc.make_a_move_from_input(game_state_example_1, "(0,0),(2,1)")
    print("move made:", str(test_2[1]), "; Current State:",test_2[0]["Lines"], "\n")

    print("Test 3")
    test_3 = game_rules_n_misc.make_a_move_from_input(game_state_example_1, "(2,1),(3,2)")
    print("Current State:",test_3[0]["Lines"], "\n")

    print("Test 4")
    test_4 = game_rules_n_misc.make_a_move_from_input(game_state_example_2, "(0,2),(0,0)")
    print("Current State:", test_4[0]["Lines"], "\n")

    # test_5 should pass
    print("Test 5")
    test_5 = game_rules_n_misc.make_a_move_from_input(game_state_example_2, "(0,2),(0,3)")
    print("move made:", str(test_5[1]), "; Current State:",test_5[0]["Lines"], "\n")

elif test_input == "play":
    print("Loading game state 0")
    selected_game_state = game_state_example_0
    while True:
        player_input = input('Input command: "(x1, y1),(x2,y2)"  or type Q to quit')
        #TODO: Enforce a input type check somewhere~~
        #TODO: Create a dimension limit based on player input (essentially play_rptest.create_board())
        if player_input in ['q', 'Q']:
            print("Guess we're done here. Bye!")
            break
        next_game_state = game_rules_n_misc.make_a_move_from_input(game_state_example_0, player_input)
        selected_game_state = next_game_state
        print("Current game state:", selected_game_state[0]["Lines"])
        continue
#make_a_move_from_input(game_state_example, "(1,2),(0,3)")

#print(intersect((0,0), (2,1), (1,1), (2,0)))

#make_a_move_randomly()