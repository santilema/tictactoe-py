from controller import Controller
from ai_bots import UnbeatableBot, RandomBot
import pygame
import sys
import time

# Playing against AI?
bot_mode = "OFF"
bot_player = 2

# Features and style of the game:
screen_size = 600
screen_color = (0, 0, 0)
grid_divisions = 3
grid_color = (169, 169, 169)
player1_color = (255, 255, 255)
player2_color = (255, 215, 0)
marks_width = 3
winning_line_width = 10
winning_line_color = (255, 0, 0)

# Screen object set up
screen = pygame.display.set_mode((screen_size, screen_size))

# Instantiation of game object
game = Controller(screen_size, screen_color, grid_divisions, grid_color,
                  screen, player1_color, player2_color, marks_width,
                  winning_line_width, winning_line_color)

random_bot = RandomBot(game.model, bot_player)
unbeatable_bot = UnbeatableBot(game.model, bot_player)

# Execution loop
while 1 > 0:
    game.view.render_board()

    if (game.model.is_final_state()):
        if (game.model.winner != 0):
            game.view.draw_winner_line()
            print(f"Player {game.model.winner} wins!")
        else:
            print("It's a draw")

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (game.model.winner == 0 and
                event.button == 1):
                game.click_claim()
                game.view.render_state()
                pygame.display.update()
                if (bot_mode == "RANDOM"):
                    random_bot.random_move()
                    time.sleep(1)
                elif (bot_mode == "UNBEATABLE"):
                    unbeatable_bot.make_move()
                    time.sleep(1)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset_board()

            if event.key == pygame.K_1:
                game.view.grid_color = (255, 100, 100)
                bot_mode = "UNBEATABLE"

            if event.key == pygame.K_2:
                game.view.grid_color = (0, 0, 255)
                bot_mode = "RANDOM"

            if event.key == pygame.K_0:
                game.view.grid_color = (169, 169, 169)
                bot_mode = "OFF"


        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
