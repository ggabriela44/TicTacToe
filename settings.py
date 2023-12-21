import pygame
import pygame.locals

#window config
SIZESCREEN = WIDTH, HEIGHT = 600, 650

# przesunięcie
MARGIN_WIDTH = 50
MARGIN_HEIGHT = 100

#rozmiar komórki
CELL_SIZE = (447 // 3)

CELL_WIDTH = (WIDTH - MARGIN_WIDTH-MARGIN_HEIGHT) // 3
CELL_HEIGHT = (HEIGHT - MARGIN_HEIGHT - MARGIN_WIDTH) // 3


#in the beggining player start
# 0 - set?, 2 - ai
TURN = 1

# 0 - nobody, 1 - player, 2 - ai
WINS = 0

#flag
WIN = 0

#draw 0 - 0, 1 - X
DRAW = 0

#framerate
FPS = 60


