import pygame
from pygame.sprite import Sprite

class Snowman(Sprite):

    def __init__(self, screen):
        "initialization of the snowman"


        super(Snowman, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/snowman_image1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        #self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.bottom - 50
        self.center_y = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        "drawing the snowman"

        self.screen.blit(self.image, self.rect)

    def update_snowman(self):
        "updating sonowman's position"

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 1.5
        if self.mup and self.rect.top > self.screen_rect.top:
            self.center_y -= 1.5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += 1.5

        self.rect.centerx = self.center
        self.rect.centery = self.center_y
    def create_snowman(self):
        "making a snowman back again"

        self.center = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom - 50
