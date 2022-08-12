from model import Model
import numpy as np
import pygame

class UnbeatableBot(Model):
    def __init__(self, model, player):
        self.model = model
        self.player = player

    def minmax(self, board, depth, is_maximazing):

        if board.is_final_state():
            if (board.winner == self.player):
                return +10
            if (board.winner == 0):
                return 0
            else:
                return -10
        
        if is_maximazing:
            possible_moves = board.get_free_spaces()
            best_value = -1000
            for move in possible_moves:
                row, col = move
                current_player = 2  if board.turn % 2 == 0 else 1
                board.claim((row, col), current_player)
                best_value = max(best_value, self.minmax(board,
                                                    depth + 1,
                                                    not is_maximazing))
                board.unclaim((row, col))
            return best_value
        else:
            possible_moves = board.get_free_spaces()
            best_value = 1000
            for move in possible_moves:
                row, col = move
                current_player = 2  if board.turn % 2 == 0 else 1
                board.claim((row, col), current_player)
                best_value = min(best_value, self.minmax(board,
                                              depth + 1,
                                              not is_maximazing))
                board.unclaim((row, col))
            return best_value

    def _find_best_move(self):
        bestVal = -1000
        bestMove = (-1, -1)
        possible_moves = self.model.get_free_spaces()

        for move in possible_moves:
            row, col = move
            current_player = 2  if self.model.turn % 2 == 0 else 1
            self.model.claim((row, col), current_player)

            moveVal = self.minmax(self.model, 0, False)

            self.model.unclaim((row, col))

            if (moveVal > bestVal):
                bestMove = (row, col)
                bestVal = moveVal
        return bestMove


    def make_move(self):
        if (self.model.turn % 2 == self.player % 2):
            self.model.claim(self._find_best_move(), self.player)