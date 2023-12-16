import pygame
import settings as s

pygame.init()

#icon config
pygame.display.set_icon(s.icon)

#font config
font = pygame.font.SysFont("Courier New", 40)

#main game loop
run = True
while run:

    s.clock.tick(s.FPS)

    #draw background
    scaled_bg = pygame.transform.scale(s.bg_image, s.SIZESCREEN)
    s.screen.blit(scaled_bg, (0, 0))
    s.screen.blit(s.stick1, (50, 100))
    s.screen.blit(s.stick2, (450, 100))
    s.screen.blit(s.stickh1, (60, 100))
    s.screen.blit(s.stickh2, (60, 450))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    pygame.display.update()

pygame.quit()