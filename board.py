import pygame, sys
import pygame.locals
from settings import *

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZESCREEN)
        pygame.display.set_caption("Kółko i Krzyżyk")

        self.bg_image = pygame.image.load("./images/background_wood.png").convert_alpha()
        self.icon = pygame.image.load("./images/bamboo_X.png").convert_alpha()
        self.stick1 = pygame.image.load("images/bamboo_stick1.png").convert_alpha()
        self.stick2 = pygame.image.load("images/bamboo_stick2.png").convert_alpha()
        self.stickh1 = pygame.image.load("images/bamboo_stickh1.png").convert_alpha()
        self.stickh2 = pygame.image.load("images/bamboo_stickh2.png").convert_alpha()
        self.stick1 = pygame.transform.scale(self.stick1, (30, 470))
        self.stick2 = pygame.transform.scale(self.stick2, (30, 470))
        self.stickh1 = pygame.transform.scale(self.stickh1, (470, 30))
        self.stickh2 = pygame.transform.scale(self.stickh2, (470, 30))

        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))


        #initialization icon
        pygame.display.set_icon(self.icon)

        #initialization fonts
        pygame.font.init()
        self.font = pygame.font.SysFont("Courier New", 40)

        #cells 3 x 3
        self.cells = [None] * 9

    def draw_board(self):
        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))



    def draw_net(self):
        #dać to do settings
        self.w = 50 #50
        self.h = 100 #100
        # vertical
        self.screen.blit(self.stickh1, (self.w, self.h + CELL_SIZE))
        self.screen.blit(self.stickh2, (self.w, self.h + 2 * CELL_SIZE))
        # horiziontal
        self.screen.blit(self.stick1, (self.w + CELL_SIZE, self.h ))
        self.screen.blit(self.stick2, (self.w + 2 * CELL_SIZE, self.h))
        # pygame.display.update()


    #wyszukiwanie pozycji rysowania X lub O
    def draw_cells(self):
        for col in range(3):
            for row in range(3):
                cell = self.cells[col + row * 3]
                if not cell:
                    continue
                cell_x = col * CELL_SIZE + CELL_SIZE / 2
                cell_y = row * CELL_SIZE + CELL_SIZE / 2

                #rysowanie X lub O
                self.draw_pointer(self.screen, cell, (cell_x, cell_y))

    def player_pos(self, pos_x, pos_y):
        pos_x = pos_x / CELL_SIZE
        pos_y = pos_y / CELL_SIZE
        self.cells[int(pos_x) + int(pos_y) * 3] = player_draw(True)

    def draw_pointer(self, screen,  text, center, color=(180, 180, 180)):
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        screen.blit(text, rect)

def player_draw(flag):
    return "X" if flag else "O"