"""
Author: J. Weible jweible@illinois.edu

Connects to the PZ-server to play a game of Rock, Paper, Scissors.

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


# @staticmethod
def parse_move(move: str) -> tuple:
    """In this game, a move looks like "(0,1),(2,3)". This function      
    simply extracts the 4 coordinates (and makes sure they're ints).  
    """
    match = re.fullmatch(r'\(?\((\d+),\s*(\d+)\),\s*\((\d+),\s*(\d+)\)\)?', move.strip())
    if not match:
        return False
    try:
        r1 = int(match.group(1))
        c1 = int(match.group(2))
        r2 = int(match.group(3))         
        c2 = int(match.group(4))      
          
    except ValueError:         
    # somehow a number isn't an int?         
        return (None, None), (None, None)     
    return r1, c1, r2, c2


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

    # search for a multi-round, 2-player "Rock, Paper, Scissors":
    game_id = False
    for g in result:
        print(result)
        print(g['fullname'])
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

    # game_play = input(
        # "Type 'human' if you would like to play as yourself, or type 'computer' if you would like the computer to play: ")

    custom_coords, height_limit, width_limit = create_board(4, 4)
    # create the game state
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

                # grab turn number
                print(result["current_player_turn"])

                result_to_submit = parse_move(result["history"][0]["move"])
                print(result_to_submit)
                # if result_to_submit in selected_game_state["Lines"]:


                last_move_player_one = result_to_submit

                if last_move_player_one != last_move_player_two:

                    if result['history'] != []:
                        
                        result_to_submit = parse_move(result_to_submit)
                        print(result_to_submit)
                
                    else:
                        continue

                else:
                    print("that is the last players move")

            except json.decoder.JSONDecodeError:
                print('Unexpected Server Response. Not valid JSON.')
                sleep(15)
                continue  # try again after a wait.  Is this a temporary server problem or a client bug?

            print('Update on previous move(s): ' + json.dumps(result))
            if result["match_status"] == "in play":
                turn_status = result["turn_status"]
                if turn_status == "your turn":
                    # Yea! There was much rejoicing.
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
        
        custom_coords, height_limit, width_limit = create_board(4, 4)

        selected_game_state, coordinates = game_rules_n_misc.make_a_move_randomly(
            selected_game_state, custom_coords)

        move_instruction = coordinates #"(0,0),(1,1)"
        print("\nSending my choice of", move_instruction)

        last_move_player_two = move_instruction

        if last_move_player_one != last_move_player_two:

            submit_move = session.post(url=game_server_url + "match/{}/move".format(match_id),
                                    json={"move": move_instruction})

            move_result = submit_move.json()["result"]
            print("move result: ", move_result)
            print("game state: ", selected_game_state)

            last_move_player_two = move_result
        
            if move_result["match_status"] in ["game over", "scored, final"]:
                print('Game over?  Who won?')
                print()
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
