import pygame
import sys
from Snowball import Snowball
from crazywarrior import Cwarrior
import time

def events(screen, snowman, snowballs):
    "treatment of events"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            "go right"
            if event.key == pygame.K_d:
                snowman.mright = True
            "go left"
            if event.key == pygame.K_a:
                snowman.mleft = True
            "go up"
            if event.key == pygame.K_w:
                snowman.mup = True
            "go down"
            if event.key == pygame.K_s:
                snowman.mdown = True
            "Shooting"
            if event.key == pygame.K_SPACE:
                new_snowball = Snowball(screen, snowman)
                snowballs.add(new_snowball)
        elif event.type == pygame.KEYUP:
            "stop right"
            if event.key == pygame.K_d:
                snowman.mright = False
            "stop left"
            if event.key == pygame.K_a:
                snowman.mleft = False
            "stop up"
            if event.key == pygame.K_w:
                snowman.mup = False
            "stop down"
            if event.key == pygame.K_s:
                snowman.mdown = False

def update(bg_color, screen, stats, sc, snowman, cwarriors, snowballs):
    "screen updating"

    screen.fill(bg_color)
    sc.show_score()
    for snowball in snowballs.sprites():
        snowball.draw_snawball()
    snowman.output()
    cwarriors.draw(screen)
    pygame.display.flip()

def update_snowballs(screen, stats, sc, cwarriors, snowballs):
    "updating snowballs posotions"

    snowballs.update()
    for snowball in snowballs.copy():
        if snowball.rect.bottom <= 0:
            snowballs.remove(snowball)
    collisions = pygame.sprite.groupcollide(snowballs, cwarriors, True, True)
    if collisions:
        for cwarriors in collisions.values():
            stats.score += 1 * len(cwarriors)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_snowmen()
    if len(cwarriors) == 0:
        snowballs.empty()
        create_army(screen, cwarriors)

def create_army(screen, cwarriors):
    "making an army of cwarriors"

    cwarrior = Cwarrior(screen)
    cwarrior_width = cwarrior.rect.width
    number_cwarrior_x = int((760 - 2 * cwarrior_width) / cwarrior_width)
    cwarrior_height = cwarrior.rect.height
    number_cwarrior_y = int((600 - 2 * cwarrior_height - 100) / cwarrior_height )

    for row_number in range(number_cwarrior_y - 3):
        for cwarrior_number in range(number_cwarrior_x - 1):

            cwarrior = Cwarrior(screen)
            cwarrior.x = cwarrior_width + cwarrior_width * cwarrior_number
            cwarrior.y = cwarrior_height + cwarrior_height * row_number
            cwarrior.rect.x = cwarrior.x
            cwarrior.rect.y = cwarrior.rect.height + cwarrior.rect.height * row_number
            cwarriors.add(cwarrior)

def update_cwarriors(stats, screen, sc, snowman, cwarriors, snowballs):
    "updates cwarriors position at the screen"

    cwarriors.update()
    if pygame.sprite.spritecollideany(snowman, cwarriors):
        snowman_kill(stats, screen, sc, snowman, cwarriors, snowballs)
    cwarriors_check(stats, screen, sc, snowman, cwarriors, snowballs)

def snowman_kill(stats, screen, sc, snowman, cwarriors, snowballs):
    "snowman - cwarrior conflict"
    if stats.snowmen_left >= 1:
        stats.snowmen_left -= 1
        sc.image_snowmen()
        cwarriors.empty()
        snowballs.empty()
        create_army(screen, cwarriors)
        time.sleep(1)
        snowman.create_snowman()
    else:
        stats.run_game = False
        sys.exit()

def cwarriors_check(stats, screen, sc, snowman, cwarriors, snowballs):
    "check : is army over the frontkine??"

    screen_rect = screen.get_rect()
    for cwarrior in cwarriors.sprites():
        if cwarrior.rect.bottom >= screen_rect.bottom:
            snowman_kill(stats, screen, sc, snowman, cwarriors, snowballs)
            break

def check_high_score(stats, sc):
    "searching for a new high score"

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("highscore.txt", 'w') as f:
            f.write(str(stats.high_score))
