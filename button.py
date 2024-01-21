import settings

class Button:
    def __init__(self, x, y, width, height, pygame, buttonText='Button',  onclickFunction=None, bg_color=None,
                 font_size=80, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.pygame = pygame
        self.current_cursor = None

        self.font = pygame.font.SysFont(settings.FONT, font_size)

        self.buttonSurface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.buttonSurface.fill((0, 0, 0, 0))
        if bg_color is not None:
            self.buttonSurface.fill((51, 102, 0, 150))
            self.buttonSurface.set_alpha(128)
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, settings.WHITE)

    def process(self, screen):
        mouse_pos = self.pygame.mouse.get_pos()
        result = None
        if self.current_cursor != "arrow":
            self.pygame.mouse.set_system_cursor(self.pygame.SYSTEM_CURSOR_ARROW)
            self.current_cursor = "arrow"
        if self.buttonRect.collidepoint(mouse_pos):
            if self.current_cursor != "hand":
                self.pygame.mouse.set_system_cursor(self.pygame.SYSTEM_CURSOR_HAND)
                self.current_cursor = "hand"
            if self.pygame.mouse.get_pressed(num_buttons=3)[0]:
                if self.onePress:
                    result = self.onclickFunction()
                elif not self.alreadyPressed:
                    result = self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
        return result
