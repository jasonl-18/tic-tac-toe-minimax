import numpy

SPACE_CHAR = ' '


class Grid:
    PLAYER_SYM = 'X'
    COMPUTER_SYM = 'O'

    def __init__(self, dimension):
        self.dim = dimension
        self.grid = numpy.array([f'{i}' for i in range(1, dimension**2 + 1)]).\
            reshape((dimension, dimension))
        self.avail_moves = {i for i in range(1, dimension**2 + 1)}
        self.turn_count = 0

    def __str__(self):
        sep = "\n" + '-' * (4 * self.dim - 1) + "\n"
        out = ""
        for i in range(self.dim):
            row = ""
            for j in range(self.dim):
                row += f' {self.grid[i][j]} |'
            out += row[:-1]
            if i != self.dim - 1:
                out += sep
        return out + "\n"

    def parseMove(self, move, current_player_sym):
        self.grid[(move - 1) // self.dim][(move - 1) % self.dim] = current_player_sym
        self.avail_moves.remove(move)
        self.turn_count += 1

    # -1: Player wins, 0: game tied or not over, 1: computer wins
    def detectGameState(self, player_turn):
        for i in range(3):
            if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i]) or (self.grid[i][0] == self.grid[i][1] == self.grid[i][2]):
                return -1 if player_turn else 1

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return -1 if player_turn else 1
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return -1 if player_turn else 1
        return 0 if len(self.avail_moves) == 0 else None
