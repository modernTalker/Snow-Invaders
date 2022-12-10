import pygame

class Snowball(pygame.sprite.Sprite):

    def __init__(self, screen, snowman):
        "creating a snowball in the snowman's position"

        super(Snowball, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 100, 6)
        self.color = (255, 255, 255)
        self.speed = 3.5
        self.rect.centerx = snowman.rect.centerx
        self.rect.top = snowman.rect.top
        self.y = float(self.rect.y)

    def update(self):
        "movement of a snowball up"

        self.y -= self.speed
        self.rect.y = self.y

    def draw_snawball(self):
        "drawing a snowball at the screen"

        pygame.draw.rect(self.screen, self.color, self.rect)
