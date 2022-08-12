from model import Model
import random
import numpy as np
import pygame

class RandomBot(Model):
    def __init__(self, model, player):
        self.model = model
        self.player = player

    def random_move(self):
        if (not self.model.is_final_state()):
            free_spaces = self.model.get_free_spaces()
            if (free_spaces):
                roof = len(free_spaces)
                indx = random.randint(0, (roof - 1))
                row, col = free_spaces[indx]
                self.model.claim((row, col), self.player)

class UnbeatableBot(Model):
    def __init__(self, model, player):
        self.model = model
        self.player = player

    def minmax(self, board, depth, is_maximazing):
        simulation = Model(self.model.size, self.model.grid_size)
        simulation.state = board
        if simulation.is_final_state():
            if (simulation.winner == self.player):
                return 10
            if (simulation.winner == 0):
                return 0
            else:
                return -10
        
        if is_maximazing:
            best_value = -1000
            for row in range(simulation.state.shape[0]):
                for col in range(simulation.state.shape[1]):
                    if simulation.is_free((row, col)):
                        simulation.state[row][col] = 2
                        best_value = max(best_value, self.minmax(simulation.state,
                                                            depth + 1,
                                                            not is_maximazing))
                        simulation.state[row][col] = 0
            return best_value
        else:
            best_value = 1000
            for row in range(simulation.state.shape[0]):
                for col in range(simulation.state.shape[1]):
                    if simulation.is_free((row, col)):
                        simulation.state[row][col] = 1
                        best_value = min(best_value, self.minmax(simulation.state,
                                                    depth + 1,
                                                    not is_maximazing))
                        simulation.state[row][col] = 0
            return best_value

    def _find_best_move(self, board):
        bestVal = -1000
        bestMove = (-1, -1)
    
        for row in range(board.state.shape[0]):
                for col in range(board.state.shape[1]):

                    if self.model.is_free((row, col)):
                        board.state[row][col] = 2

                        moveVal = self.minmax(self.model.state, 0, False)

                        board.state[row][col] = 0

                        if (moveVal > bestVal):
                            bestMove = (row, col)
                            bestVal = moveVal
        return bestMove


    def make_move(self):
        board = self.model
        if (not self.model.is_final_state()):
            self.model.claim(self._find_best_move(board), self.player)
            print("Move made")