import random

import pygame, sys
import pygame.locals
from settings import *


class Board:
    def __init__(self):
        self.image_draw = None
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

        self.draw_0 = pygame.image.load("images/bamboo_O.png").convert_alpha()
        self.draw_X = pygame.image.load("images/bamboo_X.png").convert_alpha()
        self.draw_0 = pygame.transform.scale(self.draw_0, (CELL_WIDTH/1.2, CELL_HEIGHT/1.2 ))
        self.draw_X = pygame.transform.scale(self.draw_X, (CELL_WIDTH/1.2, CELL_HEIGHT/1.2))

        # initialization icon
        pygame.display.set_icon(self.icon)

        # initialization fonts
        pygame.font.init()
        self.font = pygame.font.SysFont("Courier New", 40)

        # FIELD GAME 3 x 3
        self.field = [None] * 9

    # drawing board - filling backgorund image
    def draw_board(self):
        # print('draw_board') #T
        self.scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(self.scaled_bg, (0, 0))

    # drawing sticks as net
    def draw_net(self):
        # print('draw_net') #T
        # horizontal
        self.screen.blit(self.stickh1, (MARGIN_WIDTH, MARGIN_HEIGHT + CELL_HEIGHT -20))
        self.screen.blit(self.stickh2, (MARGIN_WIDTH, MARGIN_HEIGHT + 2 * CELL_HEIGHT -20))
        # vertical
        self.screen.blit(self.stick1, (MARGIN_WIDTH + CELL_WIDTH -20, MARGIN_HEIGHT ))
        self.screen.blit(self.stick2, (MARGIN_WIDTH + 2 * CELL_WIDTH -20, MARGIN_HEIGHT))

    # drawing cells and catch drawing images
    def draw_cells(self):
        # print('draw_cells') #T
        for col in range(3):
            for row in range(3):
                field = self.field[col + row * 3]
                if not field:
                    continue
                cell_x = col * CELL_WIDTH + CELL_WIDTH / 2
                cell_y = row * CELL_HEIGHT + CELL_HEIGHT / 2

                # drawing X or O on the field
                self.draw_pointer(self.screen, field, cell_x, cell_y)

    # player_move - position where player clicks on the board or position where computer plays
    def player_move(self, pos_x=None, pos_y=None, move=MOVE, mode=MODE):
        print("player_move_start") #T
        if MARGIN_WIDTH <= pos_x <= WIDTH-MARGIN_WIDTH and MARGIN_HEIGHT <= pos_y <= HEIGHT-MARGIN_HEIGHT:
            pos_x = (pos_x - MARGIN_WIDTH) // CELL_WIDTH
            pos_y = (pos_y - MARGIN_HEIGHT) // CELL_HEIGHT
            print("player_move_first_if") #T
            # fill the list
            if not self.field[int(pos_x) + int(pos_y) * 3]:
                if move == 1:
                    print("player_move_if_move==1") #T
                    self.field[int(pos_x) + int(pos_y) * 3] = "O"
                    if mode == 1:
                        return 2
                    else:
                        return 3
                elif move == 2:
                    print("player_move_if_move==2") #T
                    self.field[int(pos_x) + int(pos_y) * 3] = "X"
                    return 1
                # elif move == 3:
                #     print("abc3")
                #     position = self.computer_player_move(mode)
                #     self.field[position] = "X"
                #     return 1
            return move

    def computer_player_move(self, move=MOVE, mode=MODE):
        print("computer_player_move_start") #T
        field_copy = self.field.copy()
        if mode == 2:
            print("computer_player_move_first_if") #T
            # checking if computer can win in this move
            for position in range(len(field_copy)):
                print('for_loop_can_win') #T
                # print(f'field: ', self.field) #T
                # print(f'field_copy: ', field_copy) #T
                if field_copy[position] is not None:
                    continue
                else:
                    print('else inside for loop') #T
                    field_copy[position] = 'X'
                    print(f'field: ', self.field) #T
                    print(f'field_copy: ', field_copy) #T
                    is_winning_position = self.check_wins(field_copy)
                    if is_winning_position != 2:
                        field_copy[position] = None
                        print('pozycja nie wygrywająca') #T
                        continue
                    else:
                        print('pozycja win: ', position) #T
                        del field_copy
                        self.field[position] = "X"
                        return 1

            # checking if computer must block next oponent move
            for position in range(len(field_copy)):
                print('for_loop_must_block')  #T
                # print(f'field: ', self.field)  #T
                # print(f'field_copy: ', field_copy)  #T
                if field_copy[position] is not None:
                    continue
                else:
                    print('else inside for loop')  #T
                    field_copy[position] = 'O'
                    print(f'field: ', self.field)  #T
                    print(f'field_copy: ', field_copy)  #T
                    is_winning_position = self.check_wins(field_copy)
                    print(f'czy_pozycja_wygrywająca {is_winning_position}')
                    if is_winning_position != 1:
                        field_copy[position] = None
                        print('pozycji nie trzeba blokować') #T
                        continue
                    else:
                        print('pozycja do blokowania: ', position) #T
                        del field_copy
                        self.field[position] = "X"
                        return 1

            # making random move
            print('random_move')
            none_positions = [position for position, value in enumerate(field_copy) if value is None]
            if len(none_positions) == 0:
                return 1
            else:
                print(f'None positions: {none_positions}')
                position = random.choice(none_positions)
                self.field[position] = "X"
                print('pozycja random: ', position)
                return 1
        elif mode == 3:
            print("computer_player_move_elif") #T
            position = self.minimax(field_copy)
            del field_copy
            self.field[position] = "X"
            return 1

    def minimax(self, field):
        if None not in field:
            pass


    # drawing image on the net
    def draw_pointer(self, screen,  text,x, y):
        # print('draw_pointer') #T
        if text == "O":
            self.image_draw = self.draw_0
        elif text == "X":
            self.image_draw = self.draw_X
        screen.blit(self.image_draw, [x - 15, y + 35])

    def draw_lyrics(self, turn):
        # print('draw_lyrics') #T
        if turn == 1:
            text = "Ruch: Gracz 1"
        elif turn == 2:
            text = "Ruch: Gracz 2"
        elif turn == 3:
            text = "Ruch: Komputer"
        text = self.font.render(text, True, (180, 180, 180))
        position = text.get_rect()
        position.center = (WIDTH/2, MARGIN_HEIGHT/2)
        self.screen.blit(text, position)

    # checking wins of players
    def check_wins(self, field):
        # print('check_wins') #T
        player1 = ["O", "O", "O"]
        player2 = ["X", "X", "X"]

        def marker(x, y):
            return field[x + y * 3]

        # checking rows
        for x in range(3):
            rows = [marker(y, x) for y in range(3)]
            print(f'rows: {rows}') #T
            if rows == player1:
                return 1
            elif rows == player2:
                return 2

        # checking columns
        for y in range(3):
            cols = [marker(y, x) for x in range(3)]
            print(f'cols: {cols}') #T
            if cols == player1:
                return 1
            elif cols == player2:
                return 2

        # checking across
        across1 = [marker(x, x) for x in range(3)]
        across2 = [marker(x, abs(x-2)) for x in range(3)]
        print(f'across1: {across1}\nacross2: {across2}')
        if across1 == player1 or across2 == player1:
            return 1
        elif across1 == player2 or across2 == player2:
            return 2

        return 0

    # if player win fill black window and draw who win or remis
    def draw_score(self):
        # print('draw_score') #T
        def screen_upd(self, text):
            text = self.font.render(text, True, (180, 180, 180))
            position = text.get_rect()
            position.center = (WIDTH / 2, HEIGHT / 2)
            self.fill_black()
            self.screen.blit(text, position)
            self.update_screen()

        if self.check_wins(self.field) == 1:
            text = "Gracz 1 WYGRAŁ"
            screen_upd(self, text)
        elif self.check_wins(self.field) == 2:
            text = "Gracz 2 WYGRAŁ"
            screen_upd(self, text)
        elif None not in self.field:
            text = "REMIS!"
            screen_upd(self, text)
        else:
            return



    # set window to black
    def fill_black(self):
        self.screen.fill((0, 0, 0))

    # update screen
    def update_screen(self):
        pygame.display.flip()
