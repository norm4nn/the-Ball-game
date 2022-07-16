import random

import pygame
import Ball
import Brick
import Platform
import Screen

TOP_MARGIN = 128


class Level:
    def __init__(self, ball_position, ball_velocity, platform_velocity, drop_rate, brick_size, brick_amount):
        self.drop_rate = drop_rate
        self.ball_starting_pos = ball_position
        self.ball_velocity = ball_velocity
        self.platform_velocity = platform_velocity
        self.brick_size = brick_size
        self.brick_amount = brick_amount
        self.set_things()

    def set_things(self):
        pass



class Level1 (Level):

    def set_things(self):
        self.brick_amount = 60
        self.ball_starting_pos = Ball.BALL_STARTING_POSITION
        self.ball_velocity = Ball.BALL_VELOCITY
        self.platform_velocity = Platform.PLATFORM_VELOCITY
        self.brick_size = (Brick.BRICK_SIZE_X, Brick.BRICK_SIZE_Y)
        self.bricks_pos = [pygame.Rect(72 + i % 12 * self.brick_size[0], TOP_MARGIN + i // 12 * self.brick_size[1],
                                       self.brick_size[0], self.brick_size[1]) for i in range(self.brick_amount)]
        return self.bricks_pos

    def get_objects(self):#random.randint(1,4) / 1
        return ([Ball.Ball(self.ball_starting_pos[0], self.ball_starting_pos[1])], [Brick.Brick(self.bricks_pos[i][0],
                self.bricks_pos[i][1], random.randint(1,4) , self.brick_size, self.drop_rate) for i in range(self.brick_amount)],
                Platform.Platform(self.platform_velocity))


