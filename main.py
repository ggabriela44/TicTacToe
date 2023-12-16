import sys
import pygame
import pygame.locals
from settings import *
from board import *
from game import *

if __name__ == "__main__":
    game = TicTacToe()
    game.run_game()
