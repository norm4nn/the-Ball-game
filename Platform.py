import pygame
import os.path

import Ball
import Laser
from Screen import WIDTH,HEIGHT
#platform
PLATFORM_IMAGE = pygame.image.load(os.path.join('assets', 'the_platform.png'))
PLATFORM_SIZE_X = 128
PLATFORM_SIZE_Y = 16
PLATFORM_VELOCITY = 10
PLATFORM_STARTING_POSITION = (WIDTH//2 - PLATFORM_SIZE_X//2, 7*HEIGHT//8 - PLATFORM_SIZE_Y//2)
PLATFORM = pygame.transform.scale(PLATFORM_IMAGE, (PLATFORM_SIZE_X, PLATFORM_SIZE_Y))
SIZE_LEVEL_CAP = 4
LENGTH_MODIFIER = 5/4
STARTING_AMMO = 3
LASER_COOLDOWN = 1# second

class Platform():
    def __init__(self, velocity = PLATFORM_VELOCITY,  x = PLATFORM_STARTING_POSITION[0], y = PLATFORM_STARTING_POSITION[1]):
        self.rect = pygame.Rect(x,y,PLATFORM_SIZE_X,PLATFORM_SIZE_Y)
        self.image = PLATFORM
        self.velocity = velocity
        self.size_level = 0 # counter of modifying length of the platform
        self.ammo_current = STARTING_AMMO
        self.laser_cooldown = LASER_COOLDOWN
        self.laser_stopper = 0
        self.laser_on_cooldown = False
        self.down_rect = pygame.Rect(x,self.rect.y+self.rect.height//2,self.rect.width,self.rect.height//2)


    def draw(self,WINDOW):
        WINDOW.blit(self.image,self.rect)


    def update_image(self):
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))


    def apply_drop(self, drop, balls, ammo_counter):
        if drop == 0:#laser
            self.ammo_current += 1
            ammo_counter.counter += 1
        elif drop == 1 and self.size_level < SIZE_LEVEL_CAP:#length up
            self.size_level += 1
            self.rect.width *= LENGTH_MODIFIER
            self.down_rect.width *= LENGTH_MODIFIER
            self.update_image()
        elif drop == 2 and len(balls) < 20:#adding balls
            n = len(balls)
            for i in range(n):
                ball1 = Ball.Ball(balls[i].rect.x, balls[i].rect.y, balls[i].velocity)
                ball2 = Ball.Ball(balls[i].rect.x, balls[i].rect.y, balls[i].velocity)
                ball1.direction = [balls[i].direction[0] * Ball.DEVIATION1, balls[i].direction[1] * Ball.DEVIATION2]
                ball2.direction = [balls[i].direction[0] * Ball.DEVIATION2, balls[i].direction[1] * Ball.DEVIATION1]
                balls.append(ball1)
                balls.append(ball2)
            pass#3 balls
        elif drop == 3:# length down/ short up ;)
            self.size_level -= 1
            self.rect.width *= 1/LENGTH_MODIFIER
            self.down_rect.width *= 1/LENGTH_MODIFIER
            self.update_image()



    def update(self, dt, keys_pressed, lasers, ammo_counter):

        if keys_pressed[pygame.K_a] and self.rect.x > 0:  # LEFT
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.rect.width < WIDTH:  # RIGHT
            self.rect.x += self.velocity

        if self.laser_on_cooldown:
            self.laser_stopper += dt

        if self.laser_stopper >= self.laser_cooldown :
            self.laser_on_cooldown = False



        if keys_pressed[pygame.K_SPACE] and not self.laser_on_cooldown and self.ammo_current > 0:
            self.ammo_current -= 1
            ammo_counter.counter -= 1
            self.laser_on_cooldown = True
            self.laser_stopper = 0
            laser_object = Laser.Laser()
            laser_object.shoot(self.rect)
            lasers.append(laser_object)



