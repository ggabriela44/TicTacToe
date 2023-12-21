import pygame, sys
import pygame.locals
from settings import *

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZESCREEN)
        pygame.display.set_caption("Kółko Krzyżyk")

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

        self.draw_0 =  pygame.image.load("images/bamboo_O.png").convert_alpha()
        self.draw_X =  pygame.image.load("images/bamboo_X.png").convert_alpha()
        self.draw_0 = pygame.transform.scale(self.draw_0, (CELL_SIZE, CELL_SIZE ))
        self.draw_X = pygame.transform.scale(self.draw_X, (CELL_SIZE , CELL_SIZE))

        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))


        #initialization icon
        pygame.display.set_icon(self.icon)

        #initialization fonts
        pygame.font.init()
        self.font = pygame.font.SysFont("Courier New", 40)

        #FIELD GAME 3 x 3
        self.field = [None] * 9

    # drawing board - filling backgorund image
    def draw_board(self):
        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))


    #drawing sticks as net
    def draw_net(self):
        # vertical
        #prawo-lewo
        self.screen.blit(self.stickh1, (MARGIN_WIDTH, MARGIN_HEIGHT + CELL_SIZE))
        self.screen.blit(self.stickh2, (MARGIN_WIDTH, MARGIN_HEIGHT + 2 * CELL_SIZE))
        # horiziontal
        #gora - dol
        self.screen.blit(self.stick1, (MARGIN_WIDTH + CELL_SIZE, MARGIN_HEIGHT ))
        self.screen.blit(self.stick2, (MARGIN_WIDTH + 2 * CELL_SIZE, MARGIN_HEIGHT))
        # pygame.display.update()

    #drawing cells and catch drawing images
    def draw_cells(self):
        for col in range(3):
            for row in range(3):
                #
                field = self.field[col+ row * 3]
                if not field:
                    continue
                cell_x = (col+0.1) * CELL_WIDTH + CELL_WIDTH/2
                cell_y = (row+0.1) * CELL_HEIGHT + CELL_HEIGHT/2
                cell_x2 = col * CELL_SIZE + CELL_SIZE / 2
                cell_y2= row * CELL_SIZE + CELL_SIZE / 2


                #rysowanie X lub O V2
                # self.draw_pointer(self.screen, field, (cell_x, cell_y))
                self.draw_player(cell_x, cell_y, DRAW)

    #position where player click on the board
    def player_pos(self, pos_x, pos_y):

        if pos_x >= MARGIN_WIDTH and pos_x <= WIDTH-MARGIN_WIDTH and pos_y >= MARGIN_HEIGHT and pos_y <= HEIGHT-MARGIN_HEIGHT:
            pos_x = (pos_x / CELL_SIZE)-1
            pos_y = (pos_y/CELL_SIZE)-1
        # if pos_x >=50 and pos_y >=100:
        #     pos_x = pos_x/( CELL_WIDTH / 2 )   #/ MARGIN_WIDTH /3.8
        #     pos_y = pos_y/(CELL_HEIGHT / 2)    #/ MARGIN_HEIGHT/3
            # fill the field X or 0
            self.field[int(pos_x) + int(pos_y) * 3] = player_draw(DRAW)

    # def draw_pointer(self, screen,  text, center, color=(180, 180, 180)):
        # text = self.font.render(text, True, color)
        # rect = text.get_rect()
        # rect.center = center
        # screen.blit(text, rect)

    #drawing image on the net
    def draw_player(self, x, y, flag):
        if flag == 0:
            self.image_draw = self.draw_0
        elif flag == 1:
            self.image_draw = self.draw_X

        self.screen.blit(self.image_draw, [x, y])

#filing the FIELD_GAME as self.field with "1" or "0"
def player_draw(flag):
    return "1" if flag else "0"