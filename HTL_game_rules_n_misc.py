
import random
import copy
import numpy as np
import copy
import json
from os import error
from datetime import datetime
from random import shuffle,choice



# one line drawn by any player is represented as: [(0,0), (0,1), (0,2), (0,3)], [(2,0), (2,1), (2,2), (2,3)], etc.

# TODO: Build a game rule on this data structure:
# It is assumed that everything in the game_state is a legal move

# For learning: "(0,0),(2,1)" : 50

# "".join(game_state)

# only look back one turn
# move_syntax = "(0,0),(2,1)"

# Steps:
# 1. A function that deals with the geometrical problem of intersections
# - We can reference any online source as long as it is cited.
# - https://stackoverflow.com/questions/3252194/numpy-and-line-intersections

# 2. A function that searches for legal moves (thru rule of elimination)
# - When there is 0 legal move left, the game is over

# 3. Do not reinvent the wheel. Line 111 in https://github.com/iSchool-597DS/GameClientExamples/blob/master/play_rps.py
# is exactly what we are expected to expand on


# References used:
# - https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
# - https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
# - https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# - https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
def counter_clockwise(A, B, C):
    return (C[0] - A[0]) * (B[1] - A[1]) > (B[0] - A[0]) * (C[1] - A[1])


def Area2(A, B, C):
    return (B[1] - A[1]) * (C[0] - A[0]) - (C[1] - A[1]) * (B[0] - A[0])


def IsOnLeft(A, B, C):
    return Area2(A, B, C) > 0


def IsOnRight(A, B, C):
    return Area2(A, B, C) < 0


def IsCollinear(A, B, C):
    return Area2(A, B, C) == 0


def IsOverlapping(A, B, C):
    # Line AB is the Anchor
    crossproduct = (C[0] - A[0]) * (B[1] - A[1]) - (C[1] - A[1]) * (B[0] - A[0])
    if abs(crossproduct) != 0:
        return False

    dotproduct = (C[1] - A[1]) * (B[1] - A[1]) + (C[0] - A[0]) * (B[0] - A[0])
    if dotproduct < 0:
        return False

    squaredlengthba = (B[1] - A[1]) * (B[1] - A[1]) + (B[0] - A[0]) * (B[0] - A[0])
    if dotproduct > squaredlengthba:
        return False

    return True


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    # return counter_clockwise(A, C, D) != counter_clockwise(B, C, D) \
    #       and counter_clockwise(A, B, C) != counter_clockwise(A, B, D)
    if IsOnLeft(A, B, C) and IsOnRight(A, B, D):
        return True
    elif IsOnLeft(A, B, D) and IsOnRight(A, B, C):
        return True
    elif B == C and (IsOverlapping(A, B, D) or IsOverlapping(B, D, A)):
        return True
    elif A == C and IsOverlapping(A, D, B):
        return True

    return False

def formatter(a,b):
    return str(a).replace(" ","")+","+str(b).replace(" ","")



game_state_example_1 = {
    "Lines": [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (1, 1)],
    "Weights": []
    # Without learning, the 'Weights' start out empty. Might need to loop through it to assign them.
}

#print("Test inter", intersect((1, 1), (0, 1), (3, 2), (3, 1)))
#TODO: This can be merged with Sam's create_board function to provide board_coordinates based on user input

# board_coordinates = [(x, y) for x in range(4) for y in range(0, 4)]
def make_a_move_randomly(game_state, board_coordinates):
    possible_coordinates = [x for x in board_coordinates if x not in game_state['Lines']]
    shuffle(possible_coordinates)

    intersection = False
    position = choice([0,1])
    if len(game_state['Lines'])==0:
        game_state['Lines'].append((0,0))
        game_state['Lines'].append(possible_coordinates[1])
        print(game_state['Lines'], formatter(game_state["Lines"][0], game_state["Lines"][1]))
        return game_state, formatter(game_state["Lines"][0], game_state["Lines"][1])

    if (position == 0):
        print("Making a move at the Head")
        for coordinates in possible_coordinates:
            intersection = False
            for p1, p2 in zip(game_state["Lines"][::-1][:-1], game_state["Lines"][::-1][1:]):
                intersection = intersect(game_state["Lines"][0], coordinates, p1, p2)
                if intersection == True:
                    break
            if intersection == False:
                game_state["Lines"].insert(0, coordinates)
                return game_state,formatter(game_state["Lines"][0],game_state["Lines"][1])
        print("No Valid moves from present state")

    elif (position == 1):
        print("Making a move at the Tail")
        for coordinates in possible_coordinates:
            intersection = False
            for p1, p2 in zip(game_state["Lines"][::-1][:-1], game_state["Lines"][::-1][1:]):
                intersection = intersect(game_state["Lines"][-1], coordinates, p1, p2)
                if intersection == True:
                    break
            if intersection == False:
                game_state["Lines"].append(coordinates)
                return game_state,formatter(game_state["Lines"][0],game_state["Lines"][1])
        print("No Valid moves from present state")
    return game_state,None

def is_game_over(game_state,board_coordinates):
    possible_coordinates = [x for x in board_coordinates if x not in game_state['Lines']]
    # num_possible_moves = []
    num_possible_moves = 0
    for coordinates in possible_coordinates:
        intersection = False
        for p1, p2 in zip(game_state["Lines"][::-1][:-1], game_state["Lines"][::-1][1:]):
            intersection = intersect(game_state["Lines"][-1], coordinates, p1, p2)
            if intersection == True:
                break
        if intersection == False:
            num_possible_moves += 1
    #TODO: Evaluate whether it is better for num_possible_moves to be a list of moves instead of just a counter

    if num_possible_moves > 0:
        print("Still", num_possible_moves, "possible moves left.")
        return False, num_possible_moves
    elif num_possible_moves == 0:
        print("No possible moves left. The game is over.")
        return True, num_possible_moves


def make_a_move_from_input(game_state, move_syntax, height_limit, width_limit):
    print("move syntax = ",move_syntax[1])
    move_parsed = eval(move_syntax)
    print("Move Parsed = ",move_parsed )

    if move_parsed[0][0] < 0 or move_parsed[0][1] < 0 or move_parsed[1][0] < 0 or move_parsed[1][1] < 0:
        print("INVALID MOVE: Coordinates cannot be negative integers!")
        return None

    if move_parsed[0][0] > height_limit or move_parsed[1][0] > height_limit:
        print("INVALID MOVE: Height limit exceeded by", move_parsed[0] - height_limit)
        return None

    if move_parsed[0][1] > width_limit or move_parsed[1][1] > width_limit:
        print("INVALID MOVE: Width limit exceeded by", move_parsed[1] - width_limit)
        return None

    if len(game_state["Lines"]) == 0:
        print("LEGAL MOVE: First move in the game")
        game_state["Lines"].append(move_parsed[0])
        game_state["Lines"].append(move_parsed[1])
        return game_state, str(move_syntax)

    # if move_parsed not in game_state["Lines"]:
    if move_parsed[0] == game_state["Lines"][0] and move_parsed[1] not in game_state["Lines"]:
        for ele_idx, ele_value in enumerate(game_state["Lines"][:-1]):
            if intersect(game_state["Lines"][ele_idx], game_state["Lines"][ele_idx + 1], game_state["Lines"][0],
                         move_parsed[1]):
                print("INVALID MOVE: Intersecting lines!:",
                      "Line*", game_state["Lines"][ele_idx], game_state["Lines"][ele_idx + 1], "*",
                      "crossed with Line *", game_state["Lines"][0], move_parsed[1], "*")
                #return game_state, move_syntax
                print("Current game state:", game_state["Lines"])
                return None
        print("LEGAL MOVE: At head endpoint")
        game_state["Lines"].insert(0, move_parsed[1])

    elif move_parsed[0] == game_state["Lines"][-1] and move_parsed[1] not in game_state["Lines"]:
        for ele_idx, ele_value in enumerate(game_state["Lines"][:-1]):
            if intersect(game_state["Lines"][ele_idx], game_state["Lines"][ele_idx + 1], game_state["Lines"][-1],
                         move_parsed[1]):
                print("INVALID MOVE: Intersecting lines!:",
                      "Line*", game_state["Lines"][ele_idx], game_state["Lines"][ele_idx + 1], "*",
                      "crossed with Line *", game_state["Lines"][-1], move_parsed[1], "*")
                print("Current game state:", game_state["Lines"])
                #return game_state, move_syntax
                return None
        print("LEGAL MOVE: At tail endpoint")
        game_state["Lines"].append(move_parsed[1])

    else:
        print("INVALID MOVE: NO CHANGES MADE")

    return game_state, str(move_syntax)
    # print(game_state)
    # visualize_game(game_state)


def human_player_move():
    # TODO: Complete this function
    print("Please input your moves in the form of '(x1, y1), (x2, y2)'")
    player_input = input()
    return player_input


def visualize_game(game_state):
    # TODO: Determine whether this thing is needed at all.
    board_for_printing = [["-", "-", "-", "-"],
                          ["-", "-", "-", "-"],
                          ["-", "-", "-", "-"],
                          ["-", "-", "-", "-"]]
    for each_col_value in game_state["Lines"]:
        board_for_printing[each_col_value[0]][each_col_value[1]] = "*"
    iterator = 0
    for i in range(0, len(board_for_printing)):
        print(board_for_printing[iterator])
        iterator += 1