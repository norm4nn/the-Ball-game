
from Screen import WIDTH,HEIGHT
import pygame


def update(dt,balls, platform, bricks, drops, lasers, ammo_counter):
    keys_pressed = pygame.key.get_pressed()
    ammo_counter.update()

    platform.update(dt, keys_pressed, lasers, ammo_counter)

    there_is_ball = False
    balls_to_pop = []
    deleted = 0
    for i, ball in enumerate(balls):
        ball.update(dt, platform, bricks, drops)
        if ball.rect.y <= HEIGHT:
            there_is_ball = True
        else:
            balls_to_pop.append(i)
    for index in balls_to_pop:
        balls.pop(index - deleted)
        deleted += 1

    if not there_is_ball:
        return (False, True, False)

    for i, laser in enumerate(lasers):
        laser.update(bricks, drops)

    for i, drop in enumerate(drops):
        drop_touched = drop.update(platform.rect)
        if drop_touched != None:
            if drop_touched != -1:
                platform.apply_drop(drop_touched, balls, ammo_counter)
            drops.pop(i)
    #print(len(bricks))
    if len(bricks) <= 0:
        return (False, False, True)



    return (True, False, False)