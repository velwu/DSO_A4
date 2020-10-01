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

# from A5_prototype.HTL_vel_game_rules_n_misc_draft import create_board, human_player_move, intersect, make_a_move_from_input, make_a_move_randomly, visualize_game
import requests
import docopt
from random import choice, choices, randint
import json
from time import sleep
import logging
import os
os.system("python HTL_game_rules_n_misc.py")
# logging.basicConfig(level=logging.DEBUG)


def create_board(height, width):
    board_as_list = []
    for h in range(height):
        for w in range(width):
            board_as_list.append((h, w))
    return board_as_list

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
        # print(result)
        # print(g['fullname'])
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

    # generate the board dynamically
    game_board = create_board(int(input("Enter the height of the board: ")), int(input("Endter the width of the board: ")))
    print(game_board)

    # create the game state
    game_state = {
        "Lines": game_board,
        "Weights": []}

    # allow user to specify type of game
    type_of_game = input("Enter either 'person' if you would like to enter the moves, or 'computer' if you would like the computer to enter the moves: ").lower()
    print(type_of_game)

    while True:
        # wait for my turn:
        while True:
            print('\n\nrequesting await-turn now.')
            await_turn = session.get(
                url=game_server_url + "match/{}/await-turn".format(match_id))
            print(await_turn.text)
            try:
                result = await_turn.json()["result"]
                print(result)
                # here is where we get the enemy move, which we can take as input
                try:
                    if result[0]['turn_number'] != 1:
                        previous_move = result["history"][0]["move"]
                        print("Results for last move: ", previous_move, type(previous_move))
                        print()
                    else:
                        continue
                except KeyError:
                    print("Other Player not connected yet")
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

        print(visualize_game(game_state=game_state))

        if type_of_game == 'person':

            # call move functions, with game state and play move as args
            human_move = make_a_move_from_input(game_state, human_player_move())
            
            # this will be sent to the server
            move_instruction = human_move
            print("\nSending my choice of", move_instruction)

            submit_move = session.post(url=game_server_url + "match/{}/move".format(match_id),
                                       json={"move": move_instruction})
            move_result = submit_move.json()["result"]
            print(move_result)
            if move_result["match_status"] in ["game over", "scored, final"]:
                print('Game over?  Who won?')
                break

        if type_of_game == 'computer':

            # call move functions, with game state and play move as args
            computer_move = make_a_move_from_input(game_state, make_a_move_randomly(game_state))

            # this will be sent to the server
            move_instruction = computer_move
            print("\nSending my choice of", move_instruction)

            submit_move = session.post(url=game_server_url + "match/{}/move".format(match_id),
                                    json={"move": move_instruction})
            move_result = submit_move.json()["result"]
            print(move_result)
            if move_result["match_status"] in ["game over", "scored, final"]:
                print('Game over?  Who won?')
                break

        """Insert a small delay to reduce the chance of cPanel server throttling 
        this client, and to simulate the "thinking time" of a more challenging game."""
        sleep(3)

    return


if __name__ == '__main__':

    opt = docopt.docopt(__doc__)
    # print(opt)
    netid = opt.get('<netid>')
    player_key = opt.get('<player_key>')
    game_server = opt.get('--server')

    play_rps(game_server, netid, player_key)
