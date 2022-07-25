import copy
import random
from Grid import *
def minimax (grid, depth, alpha, beta, maxer):
    state = grid.detectGameState(maxer)
    if depth == 0 or (state is not None):
        return state

    if maxer:
        maxState = -10
        for move in grid.avail_moves:
            temp_grid = copy.deepcopy(grid)
            temp_grid.parseMove(move, Grid.COMPUTER_SYM)
            current_state = minimax(temp_grid, depth - 1, alpha, beta, False)
            maxState = max(current_state, maxState)
            alpha = max(current_state, alpha)
            if beta <= alpha:
                break
        return maxState

    else:
        minState = 10
        for move in grid.avail_moves:
            temp_grid = copy.deepcopy(grid)
            temp_grid.parseMove(move, Grid.PLAYER_SYM)
            current_state = minimax(temp_grid, depth - 1, alpha, beta, True)
            minState = min(minState, current_state)
            beta = min(current_state, beta)
            if beta <= alpha:
                break
        return minState

def bestMove (grid):
    if (grid.turn_count == 0):
        return 5
    output_move = -1
    currentBest = -10
    for move in grid.avail_moves:
        temp_grid = copy.deepcopy(grid)
        temp_grid.parseMove(move, Grid.COMPUTER_SYM)
        current_state = minimax(temp_grid, grid.dim**2 - grid.turn_count - 1, -10, 10, False)
        print(f'{move} : {current_state}')
        if current_state > currentBest:
            output_move = move
            currentBest = current_state

    return output_move
def randomSlot(grid):
    return random.choice(list(grid.avail_moves))