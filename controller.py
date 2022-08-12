from model import Model
from view import View
import pygame

class Controller:

    def __init__(self, size, screen_color, grid_size, grid_color, screen, player1_color,
                 player2_color, marks_width, winning_line_width,
                 winning_line_color):
        self.model = Model(size, grid_size)
        self.view = View(self.model, screen, screen_color, grid_color, player1_color,
                         player2_color, marks_width, winning_line_width,
                         winning_line_color)
        self.grid_color = grid_color

    def click_claim(self):
        mouse_position = pygame.mouse.get_pos()
        row, col = self.model.in_which_square((mouse_position))

        if (self.model.turn % 2 == 0):
            player = 2
        else:
            player = 1

        if self.model.is_free((row, col)):
            self.model.claim((row, col), player)
        else:
            print('Spot is taken, please select another one')

    def reset_board(self):
        self.model.turn = 1
        self.model.winner = 0
        for row in range(self.model.state.shape[0]):
            for col in range(self.model.state.shape[1]):
                self.model.state[row][col] = 0
