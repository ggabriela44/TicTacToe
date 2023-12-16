import pygame

#window config
SIZESCREEN = WIDTH, HEIGHT = 600, 550
screen = pygame.display.set_mode(SIZESCREEN)
pygame.display.set_caption("TicTacToe")


#framerate
FPS = 60
clock = pygame.time.Clock()


bg_image = pygame.image.load("./images/background_wood.png").convert_alpha()
icon = pygame.image.load("./images/bamboo_X.png").convert_alpha()
stick1 = pygame.image.load("images/bamboo_stick1.png").convert_alpha()
stick2 = pygame.image.load("images/bamboo_stick2.png").convert_alpha()
stickh1 = pygame.image.load("images/bamboo_stickh1.png").convert_alpha()
stickh2 = pygame.image.load("images/bamboo_stickh2.png").convert_alpha()

#drawing lines
stick1 = pygame.transform.scale(stick1, (25, 400))
stick2 = pygame.transform.scale(stick2, (25, 400))
stickh1 = pygame.transform.scale(stickh1, (400, 25))
stickh2 = pygame.transform.scale(stickh2, (400, 25))


