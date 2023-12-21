import sys
import pygame
import pygame.locals
from settings import *
from board import *
class TicTacToe:

    def __init__(self):
        pygame.init()
        # pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = Board()

    def run_game(self):
        global DRAW
        while self.running:
            self.board.draw_board()
            self.board.draw_net()
            self.board.draw_cells()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    if TURN == 1: #player
                        x, y = pygame.mouse.get_pos()
                        self.board.player_pos(x, y)
                        # # # for testing
                        # if self.board.draw_XO == 0:
                        #     self.board.draw_XO = 1
                        # elif self.board.draw_XO == 1:
                        #     self.board.draw_XO = 0


            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
