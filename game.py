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
        while self.running:
            self.board.draw_board()
            self.board.draw_net()
            pygame.display.update()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
