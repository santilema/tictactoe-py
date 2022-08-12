from model import Model
import numpy as np
import pygame


class View(Model):

    def __init__(self, model, screen, screen_color, grid_color, player1_color, player2_color,
                 marks_width, winning_line_width, winning_line_color):
        self.model = model
        self.screen = screen
        self.screen_color = screen_color
        self.grid_color = grid_color
        self.player1_color = player1_color
        self.player2_color = player2_color
        self.marks_width = marks_width
        self.winning_line_width = winning_line_width
        self.winning_line_color = winning_line_color

    def render_grid(self):
        x = 0
        gap = self.model.size / self.model.grid_size
        for n in range(1, self.model.grid_size):
            x = n * gap
            pygame.draw.line(self.screen, self.grid_color, (x, 0),
                             (x, self.model.size), 1)
            pygame.draw.line(self.screen, self.grid_color, (0, x),
                             (self.model.size, x), 1)

    def render_state(self):  # Move to view
        for row in range(self.model.state.shape[0]):
            for col in range(self.model.state.shape[1]):

                # square coordinates
                square_size = self.model.size // self.model.grid_size
                square_center = (
                    (square_size / 2) + (square_size * col),  # x-axis center
                    (square_size / 2) + (square_size * row))  # y-axis center
                s1 = (
                    square_size * col,  # top-left corner of the square
                    square_size * row)
                s2 = (
                    (square_size * col) + square_size,  # top-right corner
                    (square_size * row))
                s3 = (
                    (square_size * col),  # bot-left corner
                    (square_size * row) + square_size)
                s4 = (
                    (square_size * col) + square_size,  # bot-right corner
                    (square_size * row) + square_size)

                if (self.model.state[row][col] == 1):
                    pygame.draw.circle(self.screen,
                                       self.player1_color,
                                       square_center,
                                       (square_size / 2) - 2,
                                       width=self.marks_width)
                if (self.model.state[row][col] == 2):
                    pygame.draw.line(self.screen,
                                     self.player2_color,
                                     s1,
                                     s4,
                                     width=self.marks_width)
                    pygame.draw.line(self.screen,
                                     self.player2_color,
                                     s3,
                                     s2,
                                     width=self.marks_width)

    def draw_winner_line(self):
        line_height = (self.model.size / self.model.grid_size) / 2
        level_height = self.model.size / self.model.grid_size
        dir, order = self.model.winning_line
        if (dir == 'row'):
            start_pos = (0, line_height + (level_height * order))
            end_pos = (self.model.size,
                       line_height + (level_height * order))
            pygame.draw.line(self.screen,
                             self.winning_line_color,
                             start_pos,
                             end_pos,
                             width=self.winning_line_width)
        if (dir == 'col'):
            start_pos = (line_height + (level_height * order), 0)
            end_pos = (line_height + (level_height * order),
                       self.model.size)
            pygame.draw.line(self.screen,
                             self.winning_line_color,
                             start_pos,
                             end_pos,
                             width=self.winning_line_width)
        if (dir == 'dia'):
            if (order == 0):
                start_pos = (0, 0)
                end_pos = (self.model.size, self.model.size)
            if (order == 1):
                start_pos = (self.model.size, 0)
                end_pos = (0, self.model.size)
            pygame.draw.line(self.screen,
                             self.winning_line_color,
                             start_pos,
                             end_pos,
                             width=self.winning_line_width)

    def render_board(self):
        self.screen.fill(self.screen_color)
        self.render_grid()
        self.render_state()