import collections
import random
import time

import pygame
import Ball
import Brick
import Platform
import Update
import Screen
import Draw
import LostScreen
import Level
import Counter

pygame.init()

SLEEP_TIME = 500

def reset_lvl():
    level1 = Level.Level1([0, 0], 0, 0, 50, [0, 0], 0)
    level1.set_things()
    balls, bricks, platform = level1.get_objects()
    # drops
    drops = []
    # lasers
    lasers = []
    ammo_counter = Counter.Counter("AMMO: ", platform.ammo_current)
    return balls, bricks, platform, drops, lasers, ammo_counter


def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

#window
WINDOW = pygame.display.set_mode((Screen.WIDTH,Screen.HEIGHT))
pygame.display.set_caption(Screen.TITLE)
FPS = Screen.FPS
start_screen = LostScreen.Scene("YOU WANNA PLAY?", ['YES', 'NO'])
lost_screen = LostScreen.Scene("YOU LOST, CONTINUE?", ['YES', 'NO'])
win_screen = LostScreen.Scene("YOU WON, WANNA PLAY AGAIN?", ['YES', 'NO'])



def main():
    new_order = None
    end_game = False
    while new_order == None and not end_game:
        end_game = quitCheck()
        new_order = start_screen.update()
        start_screen.draw(WINDOW)
    if end_game or new_order == 1:
        return
    pygame.time.wait(SLEEP_TIME)
    end_game = False
    while not end_game:
        balls, bricks, platform, drops, lasers, ammo_counter = reset_lvl()
        prev_time = time.time()
        run = True
        lost = False
        won = False

        #clock
        clock = pygame.time.Clock()

        while run and not end_game:
            clock.tick(FPS)

            #compute delta time
            now = time.time()
            dt = now - prev_time
            prev_time = now

            end_game = quitCheck()




            #updating
            run, lost, won = Update.update(dt, balls, platform, bricks, drops, lasers,
                                           ammo_counter)

            #drawing
            Draw.draw(WINDOW, balls, platform, bricks, drops, lasers, ammo_counter)
        #lost screen
        if lost:
            new_order = None
            while new_order == None and not end_game:
                end_game = quitCheck()
                clock.tick(FPS)
                new_order = lost_screen.update()
                lost_screen.draw(WINDOW)

            if new_order == 1:
                end_game = True

            elif new_order == 0:
                pass
        elif won:#code winning screen
            new_order = None
            while new_order == None and not end_game:
                end_game = quitCheck()
                clock.tick(FPS)
                new_order = win_screen.update()
                win_screen.draw(WINDOW)
            if new_order == 1:
                end_game = True
            elif new_order == 0:
                pass

    #now output


    pygame.quit()


if __name__ == "__main__":
    main()


