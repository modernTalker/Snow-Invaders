import pygame

class Cwarrior(pygame.sprite.Sprite):
    "One warrior class"

    def __init__(self, screen):
        "initialization of a warrior"

        super(Cwarrior, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/crazy_warrior1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        "drawing a cwarrior at the screen"

        self.screen.blit(self.image, self.rect)

    def update(self):
        "removing the army"

        self.y += 0.1
        self.rect.y = self.y

