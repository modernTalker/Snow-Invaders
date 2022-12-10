import pygame.font
from Snowman import Snowman
from pygame.sprite import Group

class Scores():
    "showing the game information"

    def __init__(self, screen, stats):
        "initialization of counting scores"

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_snowmen()

    def image_score(self):
        "from text score ----> to text image"

        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        "converts record to image"

        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        "Showing the stats at the screen"

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.snowmen.draw(self.screen)

    def image_snowmen(self):
        "counter lives"

        self.snowmen = Group()
        for snowmen_number in range(self.stats.snowmen_left):
            snowman = Snowman(self.screen)
            snowman.rect.x = 15 + snowmen_number * snowman.rect.width
            snowman.rect.y = 20
            self.snowmen.add(snowman)