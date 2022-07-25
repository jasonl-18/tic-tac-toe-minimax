import random
import numpy
import Grid
from Grid import *
import AI

GRID_DIMENSION = 3
INPUT_ERROR = "Invalid Input. Please try again:"


def validInput(valid_domain, input_message, error_message):
    user_input = int(input(input_message))
    while not (user_input in valid_domain):
        user_input = int(input(error_message))
    return user_input


player_turn = True

order_input = validInput({1, 2}, "Choose move order: First(1) and Second(2): ",
                         INPUT_ERROR)
if order_input == 2:
    player_turn = False
grid = Grid(GRID_DIMENSION)
print(grid)

winner = "Tie"
while grid.turn_count < 9:
    current_sym = Grid.PLAYER_SYM if player_turn else Grid.COMPUTER_SYM

    #player move
    if player_turn:
        player_move = validInput(grid.avail_moves,
                                 "Choose a move (Empty slot 1 - 9): ",
                                 INPUT_ERROR)
        grid.parseMove(player_move, current_sym)
        print(grid)

    #AI move
    else:
        grid.parseMove(AI.bestMove(grid), current_sym)
        print(grid)

    state = grid.detectGameState(player_turn)
    if state == 1:
        winner = "Computer"
        break
    elif state == -1:
        winner = "Player"
        break

    player_turn = not player_turn

if (winner == "Tie"):
    print("Tie")
else:
    print(winner + " wins")
