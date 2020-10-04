from os import error
import numpy as np
import copy
import json

#randomly pick the dimensions


def create_board(height, width):
    board_as_list = []
    for h in range(height):
        for w in range(width):
            board_as_list.append((h, w))
    return board_as_list

board = create_board(int(input("Enter the height: ")), int(input("Enter the width: ")))

made_moves = []
connected_moves = []


for row in board:
    for move in row:
        print("Maximum numbers are: ", dims-1,dims2-1)
        source_input = input("Enter source coordinate ex. 00 or 11: ")
        source_input = tuple(source_input)
        target_input = input("Enter target coordinate ex. 00 or 11: ")
        target_input = tuple(target_input)
        try:
            source_move = board[int(source_input[0])][int(source_input[1])]
            target_move = board[int(target_input[0])][int(target_input[1])]
            connected_moves = [source_move, target_move]
            source_int_zero = int(source_input[0])
            target_int_zero = int(target_input[0])
            source_int_one = int(source_input[1])
            target_int_one = int(target_input[1])
            
            if (source_int_zero+1 == target_int_zero or source_int_zero+2 == target_int_zero or source_int_zero+3 == target_int_zero) or (source_int_zero == target_int_zero+1 or source_int_zero == target_int_zero+2 or source_int_zero == target_int_zero+3):
                print("move within a diagonal")
                for diff in range(1, abs(source_int_zero - target_int_zero)):
                    print(diff) 
                    for diffs in range(1, abs(source_int_one - target_int_one)):
                        print(diffs)
                        print(board[diff][diffs])
                        connected_moves.insert(diff, board[diff][diffs])
                if connected_moves not in made_moves:
                    made_moves.append(connected_moves)
                    print(made_moves)
            elif source_move[0] == target_move[0] or source_move[1] == target_move[1]:
                print("move within a row or column")
                if connected_moves not in made_moves:
                    made_moves.append(connected_moves)
                    print(made_moves)  
            # if the lines cross, invalid move
            # if a move is valid but the next move is invalid, that player loses
            # previous and current have more than 1 difference, that more tuple need to be added to connected nodes. 
                # else:
                #     previous_move = None
                else:
                    print('that move is already made!')
            else:
                print("that is an invalid move!")
        except:
            print('that move is either incomplete or off the board!')
            raise error
            continue
    


