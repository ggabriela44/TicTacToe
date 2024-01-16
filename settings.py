import pygame
import pygame.locals

# window config
SIZESCREEN = WIDTH, HEIGHT = 600, 650

# framerate
FPS = 15

# przesunięcie
MARGIN_WIDTH = 50
MARGIN_HEIGHT = 100

# cells size
CELL_WIDTH = (WIDTH - MARGIN_WIDTH*2) // 3
CELL_HEIGHT = (HEIGHT - MARGIN_HEIGHT *2) // 3

# in the beggining player start
# 0 - set?, 1 - player, 2 - ai

# MODE - game mode: 1 - PvP (default), 2 - player vs computer(normal mode), 3 - player vs computer(extreme mode)
MODE = 2

# MOVE 1 - player1 (default), 2 - player2, 3 - computer //current move
MOVE = 1


# not defined functions

# 0 - nobody, 1 - player, 2 - ai
WINS = 0

# flag
WIN = 0



