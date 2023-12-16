class Textures:
    def __init__(self, pygame, background_path, stick_path, x_path, o_path, window_width, window_height, tile_size, tile_margin, stick_width, stick_height):
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (window_width, window_height))

        self.vertical_stick = pygame.image.load(stick_path)
        self.vertical_stick = pygame.transform.scale( self.vertical_stick, (stick_width, stick_height))

        self.horizontal_stick = pygame.transform.rotate(self.vertical_stick, 90)

        self.o_image = pygame.image.load(o_path)
        self.o_image = pygame.transform.scale(self.o_image, (tile_size - tile_margin, tile_size - tile_margin))

        self.x_image = pygame.image.load(x_path)
        self. x_image = pygame.transform.scale(self.x_image, (tile_size - tile_margin, tile_size - tile_margin))