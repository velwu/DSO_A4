"""
Author: J. Weible jweible@illinois.edu and amended by Sam Walkow swalkow2@illinois.edu

Connects to the PZ-server to play a game of Hold That Line.

This can be called from a command line to authenticate with an existing
authorized netid and player_key and it will query the game_types to find the
right id, then request a match and wait for opponent to compete.

The opponent might be another running instance of this program using different
credentials.

Usage:
  play_rps.py [options] <netid> <player_key>

Options:
  --server=<url>  Change the GameServer's base URL [default: https://jweible.web.illinois.edu/pz-server/games/]
  -h --help       Show this screen.

"""

import requests
import docopt
from random import choice, choices, randint
import json
from time import sleep
import logging
import HTL_game_rules_n_misc as game_rules_n_misc
import copy
import re
# logging.basicConfig(level=logging.DEBUG)


def create_board(height, width):
    board_as_list = []
    for h in range(height):
        for w in range(width):
            board_as_list.append((h, w))
    return board_as_list, height, width


def parse_string(move):
    moves_acc = []
    for index, m in enumerate(move):
        try:
            moves_int = int(m)
            moves_acc.append(moves_int)
        except ValueError:
            pass
    return (moves_acc[0], moves_acc[1]), (moves_acc[2], moves_acc[3])


def play_rps(game_server_url: str, netid: str, player_key: str):
    # start a fresh session with blank cookies:
    session = requests.Session()
    session.headers = {"Connection": "close"}  # Disables HTTP Keep-Alive

    # query the available game_types to find the RPS id:
    game_search = session.get(url=game_server_url + "game-types",
                              json={"netid": netid,
                                    "player_key": player_key})

    # TODO: there's not sufficient error checking here...
    try:
        result = game_search.json()['result']
    except Exception as e:
        print('unexpected response:')
        print(game_search.content)
        print('\nfollowed by exception:' + str(e))
        return

    # search for Hold that line:
    game_id = False
    for g in result:
        if (g['category'] == 'hold_that_line' or 'Hold That Line' in g['fullname'].lower()):
            game_id = g['id']

    if game_id:
        print('Found matching game-type: ', game_id)
    else:
        print('Game not available now.')
        exit()

    # Now request a single match of that game type:
    request_match = session.post(url=game_server_url + "game-type/{}/request-match".format(game_id),
                                 json={"netid": netid,
                                       "player_key": player_key})

    print(request_match.text)
    match_id = request_match.json()['result']['match_id']

    # This game has multiple "rounds" or "turns".  So loop through a
    # sequence of alternating between requests "await-turn" and "move":

    custom_coords, height_limit, width_limit = create_board(4, 4)
    
    game_state_example_0 = {
        "Lines": [],
        "Weights": []}

    selected_game_state = game_state_example_0

    last_move_player_one = None
    last_move_player_two = None

    while True:
        # wait for my turn:
        while True:
            print('\n\nrequesting await-turn now.')
            await_turn = session.get(
                url=game_server_url + "match/{}/await-turn".format(match_id))
            print("Waiting for the next turn: ", await_turn.text)
            print()
            try:
                result = await_turn.json()["result"]

                if result["match_status"] == "awaiting more player(s)":
                    print('match has not started yet. sleeping a bit...')

                    sleep(5)
                    continue



            except json.decoder.JSONDecodeError:
                print('Unexpected Server Response. Not valid JSON.')
                sleep(15)
                continue  # try again after a wait.  Is this a temporary server problem or a client bug?

            print('Update on previous move(s): ' + json.dumps(result))
            if result["match_status"] == "in play":
                turn_status = result["turn_status"]
                if turn_status == "your turn":
                    # Yea! There was much rejoicing.
                    if result['history'] != []:

                        # grab turn number
                        print("The current player is: ", result["current_player_turn"])
                        # print(result["history"])

                        if last_move_player_one != result["history"][0]["move"]:
                            last_move_player_one = result["history"][0]["move"]


                            result_to_parse = parse_string(last_move_player_one)
                            print("the opponent's last move was: ", result_to_parse)

                            if selected_game_state["Lines"] != []:
    
                                # swap tuple, so tuple number zero is always the connecting end point
                                if result_to_parse[1] in selected_game_state["Lines"]:
                                    temp_result = [result_to_parse[1], result_to_parse[0]]
                                    result_to_parse = temp_result
                                # front or end of the sequence
                                if result_to_parse[0] == selected_game_state["Lines"][0]:
                                    selected_game_state["Lines"].insert(0, result_to_parse[1])
                                else:
                                    selected_game_state["Lines"].append(result_to_parse[1])
                                print(selected_game_state)

                            else:
                                # append in any order if the list is empty
                                selected_game_state["Lines"].append(result_to_parse[0])
                                selected_game_state["Lines"].append(result_to_parse[1])


                    break  # exit the while loop.
                if "Timed out" in turn_status:
                    print(
                        'PZ-server said it timed out while waiting for my turn to come up...')
                print('waiting for my turn...')
                sleep(3)
                continue
            elif result["match_status"] in ["game over", "scored, final"]:
                print('Game over?  Who won?')
                return
            elif result["match_status"] == "awaiting more player(s)":
                print('match has not started yet. sleeping a bit...')
                sleep(5)
            else:
                raise ValueError('Unexpected match_status: ' +
                                 result["match_status"])

        # Ok, now it's my turn...

        # submit my move:

        copy_select_game_state = copy.deepcopy(selected_game_state)

        selected_game_state, coordinates = game_rules_n_misc.make_a_move_randomly(
            selected_game_state, custom_coords)


        if coordinates != None:
            move_instruction = coordinates  # "(0,0),(1,1)"
            print("\nSending my choice of", move_instruction)

            last_move_player_two = move_instruction


            submit_move = session.post(url=game_server_url + "match/{}/move".format(match_id),
                                       json={"move": move_instruction})

            if submit_move.json()["result"]["outcome"] == "Invalid move rejected.":
                selected_game_state = copy_select_game_state
                print("Game Stated reverted back one move")
                continue

            move_result = submit_move.json()["result"]
            print("move result: ", move_result)
            print("game state: ", selected_game_state)

            last_move_player_two = move_result

            if move_result["match_status"] in ["game over", "scored, final"]:
                print('Game over?  Who won?')
                print()
                break


        else:
            print("no more moves")
            # result["match_status"] == "game over"
            break


        sleep(3)

    return


if __name__ == '__main__':
    opt = docopt.docopt(__doc__)
    # print(opt)
    netid = opt.get('<netid>')
    player_key = opt.get('<player_key>')
    game_server = opt.get('--server')

    play_rps(game_server, netid, player_key)
