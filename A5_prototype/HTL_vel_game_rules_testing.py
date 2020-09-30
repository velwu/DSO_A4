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
test_1 = drafty.make_a_move_from_input(game_state_example_1, "(1,2),(3,1)")
print("move made:", str(test_1[1]), "; Current State:",test_1[0]["Lines"])


test_2 = drafty.make_a_move_from_input(game_state_example_1, "(0,0),(2,1)")
print("move made:", str(test_2[1]), "; Current State:",test_2[0]["Lines"])

test_3 = drafty.make_a_move_from_input(game_state_example_1, "(2,1),(3,2)")
print("Current State:",test_3["Lines"])

#make_a_move_from_input(game_state_example, "(1,2),(0,3)")

#print(intersect((0,0), (2,1), (1,1), (2,0)))

#make_a_move_randomly()