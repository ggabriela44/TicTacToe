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
        self.stick1 = pygame.transform.scale(self.stick1, (30, 450))
        self.stick2 = pygame.transform.scale(self.stick2, (30, 450))
        self.stickh1 = pygame.transform.scale(self.stickh1, (500, 30))
        self.stickh2 = pygame.transform.scale(self.stickh2, (500, 30))

        self.draw_0 =  pygame.image.load("images/bamboo_O.png").convert_alpha()
        self.draw_X =  pygame.image.load("images/bamboo_X.png").convert_alpha()
        self.draw_0 = pygame.transform.scale(self.draw_0, (CELL_WIDTH/1.2, CELL_HEIGHT/1.2 ))
        self.draw_X = pygame.transform.scale(self.draw_X, (CELL_WIDTH/1.2, CELL_HEIGHT/1.2))

        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))

        # draw 0 - 0, 1 - X
        self.draw_XO = 0

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
        # horiziontal - poziomo
        self.screen.blit(self.stickh1, (MARGIN_WIDTH, MARGIN_HEIGHT + CELL_HEIGHT -20))
        self.screen.blit(self.stickh2, (MARGIN_WIDTH, MARGIN_HEIGHT + 2 * CELL_HEIGHT -20))
        # vertical - pionowo
        self.screen.blit(self.stick1, (MARGIN_WIDTH + CELL_WIDTH -20, MARGIN_HEIGHT ))
        self.screen.blit(self.stick2, (MARGIN_WIDTH + 2 * CELL_WIDTH -20, MARGIN_HEIGHT))


        #rysowanie lini pomocniczne - do usunięcia
        # for i in range(1, 3):
        #     pygame.draw.line(self.screen, (255,255,255), (MARGIN_WIDTH + CELL_WIDTH * i, MARGIN_HEIGHT),
        #                      (MARGIN_WIDTH + CELL_WIDTH * i, HEIGHT - MARGIN_HEIGHT))
        #     pygame.draw.line(self.screen, (255,255,255), (MARGIN_WIDTH, MARGIN_HEIGHT + CELL_HEIGHT * i),
        #                      (WIDTH - MARGIN_WIDTH, MARGIN_HEIGHT + CELL_HEIGHT * i))

    #drawing cells and catch drawing images
    def draw_cells(self):
        for col in range(3):
            for row in range(3):
                field = self.field[col+ row * 3]
                if not field:
                    continue
                cell_x = (col) * CELL_WIDTH + CELL_WIDTH/2
                cell_y = (row) * CELL_HEIGHT + CELL_HEIGHT/2

                #rysowanie X lub O pomocnicznie - do usunięcia
                # self.draw_pointer(self.screen, field, (cell_x, cell_y))

                #draw "0" or "X"
                self.draw_player(cell_x, cell_y, self.draw_XO)

    #position where player click on the board
    def player_pos(self, pos_x, pos_y):

        if pos_x >= MARGIN_WIDTH and pos_x <= WIDTH-MARGIN_WIDTH and pos_y >= MARGIN_HEIGHT and pos_y <= HEIGHT-MARGIN_HEIGHT:
            pos_x = (pos_x - MARGIN_WIDTH ) // CELL_WIDTH
            pos_y = (pos_y - MARGIN_HEIGHT) // CELL_HEIGHT
            self.field[int(pos_x) + int(pos_y) * 3] = player_draw(self.draw_XO)
            # if self.draw_XO == 0:
            #     self.draw_XO = 1
            # elif self.draw_XO == 1:
            #     self.draw_XO = 0

    #funkcja pomocniczna - do usunięcia
    def draw_pointer(self, screen,  text, center, color=(180, 180, 180)):
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        screen.blit(text, rect)

    #drawing image on the net
    def draw_player(self, x, y, flag):
        if flag == 0:
            image_draw = self.draw_0
        else:
            image_draw = self.draw_X
        self.screen.blit(image_draw, [x-15, y+35])


#filing the FIELD_GAME as self.field with "1" or "0"
def player_draw(flag):
    return "1" if flag else "0"