import pygame
# from tile import Tile, TileState
import time
import board
from textures import Textures
from enum import Enum
# import display_functions
# from menu_button import MenuButton

#Configuration
pygame.init()

#flag
running = True

fps = 60
fpsClock = pygame.time.Clock()

#font config
font = pygame.font.SysFont("Courier New", 40)

#window config
window_width = 450
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))

#title window
pygame.display.set_caption("TicTacToe")


#size of tile (kwadratu albo dosłownie płytki XD)
#TODO thinking what does it
tile_size = 100

game_state = 1 #stan ekranu gry

#image config
stick_height = tile_size * 1
stick_width = tile_size * 1 / 3
tile_margin = 50

textures = Textures(pygame, './Textures/bamboo_card.jpg', './Textures/bamboo_stick.png',
                    './Textures/bamboo_x.png', './Textures/bamboo_circle.png',
                    window_width, window_height, tile_size, tile_margin, stick_width, stick_height)

#icon config
pygame.display.set_icon(textures.o_image)

# top margin XD do przyciskow
#TODO other resolve this
top_margin = 30

# set 1 message testing
# message = font.render("Hello World!!", True, ("blue"))
# screen.blit(message,(0,0))

gameboard = []












#The end
pygame.display.update()
fpsClock.tick(fps)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()