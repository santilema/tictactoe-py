import numpy as np
import random

class Model:
    def __init__(self, size, grid_size):
        self.size = size
        self.grid_size = grid_size
        self.state = np.zeros((grid_size, grid_size), dtype=np.int64)
        # self.state = np.array([[0, 0, 0], 
        #                        [0, 0, 0],
        #                        [1, 0, 2]])
        self.turn = 1
        self.winner = 0
        self.winning_line = 0

    def in_which_square(self, coordinates):
        x, y = coordinates
        square_size = self.size // self.grid_size
        
        col = x // square_size
        row = y // square_size

        return (row, col)

    def is_free(self, position):
        r, c = position
        return self.state[r][c] == 0

    def claim(self, position, player):
        if player not in [1, 2]:
            raise ValueError("Not a valid player")
        # if self.is_free(position):
        r, c = position
        self.state[r][c] = player
        self.turn += 1
        # else:
            # raise RuntimeError('Spot is taken')

    def unclaim(self, position):
        r, c = position
        self.state[r][c] = 0
        self.turn -= 1

    def get_free_spaces(self):
        free_spaces = []
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row][col] == 0:
                    free_spaces.append((row, col))
        return free_spaces

    
    def check_rows(self):
        for n in range(self.state.shape[0]):
            if (self.state[n][0] != 0 and 
            np.all(self.state[n] == self.state[n][0])):
                if self.state[n][0] == 1:
                    self.winner = 1
                else:
                    self.winner = 2
                self.winning_line = ('row', n)
                return True
        return False

    def check_columns(self):
        for col in range(self.state.shape[1]):
            current_col = []
            for row in range(self.state.shape[0]):
                current_col.append(self.state[row][col])
            if (current_col[0] != 0 and
                current_col.count(current_col[0]) == len(current_col)):
                    if current_col[0] == 1:
                        self.winner = 1
                    else:
                        self.winner = 2
                    self.winning_line = ('col', col)
                    return True
        return False

    def first_diagonal(self):
        values = []
        for xy in range(self.state.shape[0]):
            values.append(self.state[xy][xy])
        if (values[0] != 0 and
            values.count(values[0]) == len(values)):
            if values[0] == 1:
                self.winner = 1
            else:
                self.winner = 2
            return True

    def second_diagonal(self):
        values = []
        y = self.state.shape[0]
        for x in range(self.state.shape[0]):
            y -= 1
            values.append(self.state[x][y])
        if (values[0] != 0 and
            values.count(values[0]) == len(values)):
            if values[0] == 1:
                self.winner = 1
            else:
                self.winner = 2
            return True

    def check_diagonals(self):
            if self.first_diagonal():
                self.winning_line = ('dia', 0)
                return True
            elif self.second_diagonal():
                self.winning_line = ('dia', 1)
                return True
            else:
                return False

    def is_board_full(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row][col] == 0:
                    return False
        return True

    def is_final_state(self):
        return (self.check_rows() or
                self.check_columns() or
                self.check_diagonals() or
                self.is_board_full())

    def generate_random_states(self, qty, moves):
        generated_states = []
        count = qty
        while count > 0:
            scenario = Model(self.size, self.grid_size)
            for move in range(moves):
                player = 2 if move % 2 == 0 else 1
                free_spaces = scenario.get_free_spaces()
                indx = random.randint(0, len(free_spaces) - 1)
                spot = free_spaces[indx]
                scenario.claim(spot, player)
            if not scenario.is_final_state():
                generated_states.append(scenario.state)
                count -= 1

        return generated_states

            
