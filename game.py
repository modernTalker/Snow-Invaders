import pygame
import controls
from Snowman import Snowman
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((760, 600))
    pygame.display.set_caption("Snow invaders")
    bg_color = (0, 0, 0)
    snowman = Snowman(screen)
    snowballs = Group()
    cwarriors = Group()
    controls.create_army(screen, cwarriors)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:

        controls.events(screen, snowman, snowballs)
        if stats.run_game:
            snowman.update_snowman()
            controls.update(bg_color, screen, stats, sc, snowman, cwarriors, snowballs)
            controls.update_snowballs(screen, stats, sc, cwarriors, snowballs)
            controls.update_cwarriors(stats, screen, sc, snowman, cwarriors, snowballs)

run()