import pygame.locals
from settings import *
from board import *


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = Board()
        self.turn = 1
        self.move = MOVE

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    if self.move == 1:  # player
                        x, y = pygame.mouse.get_pos()
                        self.move = self.board.player_pos(x, y,  self.move)

                    elif self.move == 2:  # 2nd-player
                        x, y = pygame.mouse.get_pos()
                        self.move = self.board.player_pos(x, y,  self.move)


            self.board.draw_board()
            self.board.draw_net()
            self.board.draw_cells()
            pygame.display.update()

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

