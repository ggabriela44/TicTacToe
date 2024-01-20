import pygame.locals
import random
import settings
from settings import *
import menu


class Board:
    def __init__(self, screen, game_state):
        self.image_draw = None
        self.screen = screen
        pygame.display.set_caption("Kółko i Krzyżyk")

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
        self.draw_0 = pygame.transform.scale(self.draw_0, (CELL_WIDTH / 1.2, CELL_HEIGHT / 1.2))
        self.draw_X = pygame.transform.scale(self.draw_X, (CELL_WIDTH / 1.2, CELL_HEIGHT / 1.2))

        # initialization icon
        pygame.display.set_icon(self.icon)

        # initialization fonts
        pygame.font.init()
        # self.font = FONT
        self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)

        # FIELD GAME 3 x 3
        self.field = FIELD

        self.game_state = game_state

    # drawing board - filling background image
    def draw_board(self):
        scaled_bg = pygame.transform.scale(self.bg_image, SIZESCREEN)
        self.screen.blit(scaled_bg, (0, 0))

    # drawing sticks as net
    def draw_net(self):
        # horizontal
        self.screen.blit(self.stickh1, (MARGIN_WIDTH, MARGIN_HEIGHT + CELL_HEIGHT - 20))
        self.screen.blit(self.stickh2, (MARGIN_WIDTH, MARGIN_HEIGHT + 2 * CELL_HEIGHT - 20))
        # vertical
        self.screen.blit(self.stick1, (MARGIN_WIDTH + CELL_WIDTH - 20, MARGIN_HEIGHT))
        self.screen.blit(self.stick2, (MARGIN_WIDTH + 2 * CELL_WIDTH - 20, MARGIN_HEIGHT))

    # drawing cells and catch drawing images
    def draw_cells(self):
        for col in range(3):
            for row in range(3):
                field = self.field[col + row * 3]
                if not field:
                    continue
                cell_x = col * CELL_WIDTH + CELL_WIDTH / 2
                cell_y = row * CELL_HEIGHT + CELL_HEIGHT / 2

                # drawing X or O on the field
                self.draw_pointer(self.screen, field, cell_x, cell_y)

    # player_move - position where player clicks on the board
    def player_move(self, pos_x, pos_y, move=menu.Move.Player1, mode=menu.GameMode.PVP):
        if MARGIN_WIDTH <= pos_x <= WIDTH - MARGIN_WIDTH and MARGIN_HEIGHT <= pos_y <= HEIGHT - MARGIN_HEIGHT:
            pos_x = (pos_x - MARGIN_WIDTH) // CELL_WIDTH
            pos_y = (pos_y - MARGIN_HEIGHT) // CELL_HEIGHT
            # fill the list
            if not self.field[int(pos_x) + int(pos_y) * 3]:
                if move == menu.Move.Player1:
                    self.field[int(pos_x) + int(pos_y) * 3] = "O"
                    if mode == menu.GameMode.PVP:
                        return menu.Move.Player2
                    else:
                        return menu.Move.AI
                elif move == menu.Move.Player2:
                    self.field[int(pos_x) + int(pos_y) * 3] = "X"
                    return menu.Move.Player1
            return move

    def computer_player_move(self, mode):
        field_copy = self.field.copy()
        if mode == menu.GameMode.Normal:

            # checking if computer can win in it's move
            for position in range(len(field_copy)):
                if field_copy[position] is not None:
                    continue
                else:
                    field_copy[position] = "X"
                    is_winning_position = self.check_wins(field_copy)
                    if is_winning_position != 2:
                        field_copy[position] = None
                        continue
                    else:
                        del field_copy
                        self.field[position] = "X"
                        return menu.Move.Player1

            # checking if computer must block oponent's next move
            for position in range(len(field_copy)):
                if field_copy[position] is not None:
                    continue
                else:
                    field_copy[position] = "O"
                    is_winning_position = self.check_wins(field_copy)
                    if is_winning_position != 1:
                        field_copy[position] = None
                        continue
                    else:
                        del field_copy
                        self.field[position] = "X"
                        return menu.Move.Player1

            # making random move
            none_positions = [position for position, value in enumerate(field_copy) if value is None]
            if len(none_positions) == 0:
                return menu.Move.Player1
            else:
                position = random.choice(none_positions)
                del field_copy
                self.field[position] = "X"
                return menu.Move.Player1

        elif mode == menu.GameMode.Extreme:
            for position in range(len(field_copy)):
                if field_copy[position] is not None:
                    continue
                else:
                    value, position = self.minimax(field_copy, True)
                    self.field[position] = "X"
                    return menu.Move.Player1

    def minimax(self, field, is_maximizing):

        # checking if it is end of game
        case = self.check_wins(field)
        if case == 1:
            return -1, None
        elif case == 2:
            return 1, None
        elif None not in field:
            return 0, None

        # move of player that wants to maximize
        if is_maximizing:
            max_value = -1000
            best_move = None
            empty_positions = [position for position, value in enumerate(field) if value is None]

            for empty_position in empty_positions:
                temp_board = field.copy()
                temp_board[empty_position] = "X"
                value = self.minimax(temp_board, False)[0]

                if value > max_value:
                    max_value = value
                    best_move = empty_position
            return max_value, best_move

        # move of player that wants to minimize
        elif not is_maximizing:
            min_value = 1000
            best_move = None
            empty_positions = [position for position, value in enumerate(field) if value is None]

            for empty_position in empty_positions:
                temp_board = field.copy()
                temp_board[empty_position] = "O"
                value = self.minimax(temp_board, True)[0]

                if value < min_value:
                    min_value = value
                    best_move = empty_position
            return min_value, best_move

    # drawing image on the net
    def draw_pointer(self, screen, text, x, y):
        if text == "O":
            self.image_draw = self.draw_0
        elif text == "X":
            self.image_draw = self.draw_X
        screen.blit(self.image_draw, [x - 15, y + 35])

    def draw_lyrics(self, turn):

        if turn == menu.Move.Player1:
            text = "Ruch: Gracz 1"
        elif turn == menu.Move.Player2:
            text = "Ruch: Gracz 2"
        elif turn == menu.Move.AI:
            text = "Ruch: Komputer"

        text = self.font.render(text, True, (180, 180, 180))
        position = text.get_rect()
        position.center = (WIDTH / 2, MARGIN_HEIGHT / 2)
        self.screen.blit(text, position)

    # checking wins of players
    def check_wins(self, field):
        player1 = ["O", "O", "O"]
        player2 = ["X", "X", "X"]

        def marker(x, y):
            return field[x + y * 3]

        # checking rows
        for x in range(3):
            rows = [marker(y, x) for y in range(3)]
            if rows == player1:
                return 1
            elif rows == player2:
                return 2

        # checking columns
        for y in range(3):
            cols = [marker(y, x) for x in range(3)]
            if cols == player1:
                return 1
            elif cols == player2:
                return 2

        # checking across
        across1 = [marker(x, x) for x in range(3)]
        across2 = [marker(x, abs(x - 2)) for x in range(3)]
        if across1 == player1 or across2 == player1:
            return 1
        elif across1 == player2 or across2 == player2:
            return 2

        return 0

    # if player wins than draw who wins or remis
    def draw_score(self, turn):
        def draw(text):
            font2 = pygame.font.SysFont(settings.FONT, 50)
            text = font2.render(text, True, (255, 153, 153))
            position = text.get_rect()
            position.center = (WIDTH / 2, MARGIN_HEIGHT / 2)

            self.screen.blit(text, position)
            pygame.display.flip()
            pygame.display.update()

        if self.check_wins(self.field) == 1:
            text = "WYGRAŁ Gracz 1"
            draw(text)
            return 5

        elif self.check_wins(self.field) == 2:
            if menu.GameMode.PVP:
                text = "WYGRAŁ Gracz 2"
            elif menu.GameMode.Normal or menu.GameMode.Extreme:
                text = "WYGRAŁ Komputer"
            draw(text)
            return 5

        elif None not in self.field:
            text = "REMIS!"
            draw(text)
            return 5

        else:
            return
