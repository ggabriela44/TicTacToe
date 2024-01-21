import pygame, sys
import pygame.locals
import settings
import board
import time
import menu


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SIZESCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = menu.GameState.MainMenu
        self.board = board.Board(self.screen, self.game_state)
        self.move = menu.Move.Player1
        self.game_mode = menu.GameMode.PVP  # default pvp
        menu.add_btn()

    def run_game(self):
        while self.running:
            # PAUZA - KONIEC ROZGRYWKI
            if self.game_state == menu.GameState.Pause:
                for buttons in menu.pause_menu_buttons:
                    state = buttons.process(self.screen)
                    if state is not None:
                        self.game_state = state
                        # self.game_mode = self.game_mode
                        wait = 0.1

            # RESET GAME
            if self.game_state == menu.GameState.Reset:
                self.screen = pygame.display.set_mode(settings.SIZESCREEN)
                self.clock = pygame.time.Clock()
                self.running = True
                self.game_state = menu.GameState.MainMenu
                self.board = board.Board(self.screen, self.game_state)
                self.move = menu.Move.Player1
                self.game_mode = menu.GameMode.PVP
                self.board.image_draw = None
                settings.FIELD = [None] * 9
                self.board.field = settings.FIELD
                continue

            #REVENGE GAME
            if self.game_state == menu.GameState.Rematch:
                self.clock = pygame.time.Clock()
                self.running = True
                self.game_state = menu.GameState.Game
                self.board = board.Board(self.screen, self.game_state)
                self.move = menu.Move.Player1
                self.board.image_draw = None
                settings.FIELD = [None] * 9
                self.board.field = settings.FIELD
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.game_state == menu.GameState.Exit:
                    self.running = False

                # POCZĄTKOWE MENU
                if self.game_state == menu.GameState.MainMenu:
                    self.board.draw_board()
                    menu.draw_title(self.screen,"Kółko i Krzyżyk")
                    for buttons in menu.main_menu_buttons:
                        state = buttons.process(self.screen)
                        if state is not None:
                            self.game_state = state
                            wait = 0.5

                # MENU TRYB GRY
                elif self.game_state == menu.GameState.PlayerMenu:
                    self.board.draw_board()
                    menu.draw_title(self.screen,"Tryb rozgrywki:")
                    for button in menu.game_mode_buttons:
                        mode_btn = button.process(self.screen)
                        if mode_btn is not None:
                            self.game_state = menu.GameState.Game
                            self.game_mode = mode_btn
                            wait = 0.5

                elif self.game_state == menu.GameState.Game:
                    self.board.draw_board()
                    self.board.draw_net()
                    self.board.draw_cells()

                    pause = self.board.draw_score(self.game_mode)
                    if pause == 5:
                        self.game_state = menu.GameState.Pause
                        continue
                    else:
                        self.board.draw_lyrics(self.move)

                    # P1 VS P2
                    if self.game_mode == menu.GameMode.PVP:
                        # PLAYER
                        if event.type == pygame.locals.MOUSEBUTTONDOWN:
                            if self.move == menu.Move.Player1:  # player
                                x, y = pygame.mouse.get_pos()
                                self.move = self.board.player_move(x, y, self.move, self.game_mode)
                                if self.move is None:
                                    self.move = menu.Move.Player1
                            # PLAYER2
                            elif self.move == menu.Move.Player2:  # 2nd-player
                                x, y = pygame.mouse.get_pos()
                                self.move = self.board.player_move(x, y, self.move, self.game_mode)
                                if self.move is None:
                                    self.move = menu.Move.Player2

                    # PLAYER1 VS AI(NORMAL MODE)
                    elif self.game_mode == menu.GameMode.Normal:
                        # PLAYER
                        if event.type == pygame.locals.MOUSEBUTTONDOWN and self.move != menu.Move.AI:
                            if self.move == menu.Move.Player1:  # player
                                x, y = pygame.mouse.get_pos()
                                self.move = self.board.player_move(x, y, self.move, self.game_mode)
                                if self.move is None:
                                    self.move = menu.Move.Player1

                        # AI/COMPUTER
                        elif self.move == menu.Move.AI:
                            self.move = self.board.computer_player_move(self.game_mode)

                    # PLAYER1 VS AI(EXTREME MODE)
                    elif self.game_mode == menu.GameMode.Extreme:
                        # PLAYER
                        if event.type == pygame.locals.MOUSEBUTTONDOWN and self.move != menu.Move.AI:
                            if self.move == menu.Move.Player1:
                                x, y = pygame.mouse.get_pos()
                                self.move = self.board.player_move(x, y, self.move, self.game_mode)
                                if self.move is None:
                                    self.move = menu.Move.Player1
                        # AI/COMPUTER
                        elif self.move == menu.Move.AI:
                            self.move = self.board.computer_player_move(self.game_mode)

            pygame.display.update()

            self.clock.tick(settings.FPS)
            if settings.wait is not None:
                time.sleep(settings.wait)
                settings.wait = None

        pygame.quit()
        sys.exit()
