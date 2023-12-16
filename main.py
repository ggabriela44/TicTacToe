import pygame

pygame.init()

#window config
SIZESCREEN = WIDTH, HEIGHT = 600, 550
screen = pygame.display.set_mode(SIZESCREEN)
pygame.display.set_caption("TicTacToe")


#framerate
FPS = 60
clock = pygame.time.Clock()


bg_image = pygame.image.load("./images/background_wood.png").convert_alpha()
icon = pygame.image.load("./images/bamboo_X.png").convert_alpha()


#icon config
pygame.display.set_icon(icon)

#font config
font = pygame.font.SysFont("Courier New", 40)


#main game loop
run = True
while run:

    clock.tick(FPS)

    #draw background
    scaled_bg = pygame.transform.scale(bg_image, SIZESCREEN)
    screen.blit(scaled_bg, (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    pygame.display.update()

pygame.quit()