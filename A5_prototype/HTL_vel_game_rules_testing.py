import A5_prototype.HTL_vel_game_rules_n_misc_draft as drafty

"""
TEST CODES BELOW:
"""

# This test should be successful
game_state_example_1 = {
    "Lines": [(0,0), (0,1), (0,2), (0,3), (1,2)],
    "Weights": []
    # Without learning, the 'Weights' start out empty. Might need to loop through it to assign them.
}

game_state_example_2 = {
    "Lines": [(0,1), (0,2)],
    "Weights": []
}

# Test 1, 2, 5 should pass, while 3 and 4 should fail
print("Test 1")
test_1 = drafty.make_a_move_from_input(game_state_example_1, "(1,2),(3,1)")
print("move made:", str(test_1[1]), "; Current State:",test_1[0]["Lines"], "\n")

print("Test 2")
test_2 = drafty.make_a_move_from_input(game_state_example_1, "(0,0),(2,1)")
print("move made:", str(test_2[1]), "; Current State:",test_2[0]["Lines"], "\n")

print("Test 3")
test_3 = drafty.make_a_move_from_input(game_state_example_1, "(2,1),(3,2)")
print("Current State:",test_3["Lines"], "\n")

print("Test 4")
test_4 = drafty.make_a_move_from_input(game_state_example_2, "(0,2),(0,0)")
print("Current State:", test_4["Lines"], "\n")

# test_5 should pass
print("Test 5")
test_5 = drafty.make_a_move_from_input(game_state_example_2, "(0,2),(0,3)")
print("move made:", str(test_5[1]), "; Current State:",test_5[0]["Lines"], "\n")




#make_a_move_from_input(game_state_example, "(1,2),(0,3)")

#print(intersect((0,0), (2,1), (1,1), (2,0)))

#make_a_move_randomly()