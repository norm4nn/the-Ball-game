import Screen
import pygame


def draw(WINDOW, balls, platform, bricks, drops, lasers, ammo_counter):

    WINDOW.fill(Screen.LIGHT_BLUE)

    ammo_counter.draw(WINDOW)
    for ball in balls:
        ball.draw(WINDOW)
    platform.draw(WINDOW)

    for i in range(len(bricks)):
        WINDOW.blit(bricks[i].image, (bricks[i].rect.x, bricks[i].rect.y))

    for drop in drops:
        drop.draw(WINDOW)

    for laser in lasers:
        laser.draw(WINDOW)

    pygame.display.update()