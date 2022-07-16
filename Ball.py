
import pygame
import os.path
from Screen import WIDTH, HEIGHT
import Drop
#ball
BALL_IMAGE = pygame.image.load(os.path.join('assets','the_ball.png'))
BALL_SIZE = 16
BALL_VELOCITY = 4
BALL_STARTING_POSITION = (WIDTH//2 - BALL_SIZE//2, 3*HEIGHT//4 - BALL_SIZE//2)
BALL = pygame.transform.scale(BALL_IMAGE,(BALL_SIZE,BALL_SIZE))
BALL = pygame.transform.rotate(BALL,90)
ROTATION_SPEED = 200
DEVIATION1 = 1.18
DEVIATION2 = 0.77

class Ball:
    def __init__(self, x = BALL_STARTING_POSITION[0], y = BALL_STARTING_POSITION[1], velocity = BALL_VELOCITY):
        self.rect = pygame.Rect(x,y,BALL_SIZE,BALL_SIZE)
        self.size = BALL_SIZE
        self.image = BALL
        self.velocity = velocity
        self.direction = [1.0, 1.0]
        self.current_rotation = 0

    def draw(self,WINDOW):

        WINDOW.blit(self.image,self.rect)


    def update_rotation(self,dt):
        self.current_rotation += int(dt*ROTATION_SPEED)
        self.current_rotation %= 360
        self.image = pygame.transform.rotate(BALL, self.current_rotation)#int(dt*ROTATION_SPEED)%360)#ROTATION_SPEED*dt)



    def update(self, dt, platform, bricks, drops):
        if self.rect.x <= 0 or self.rect.x + self.size >= WIDTH:
            self.direction[0] *= -1

        if self.rect.colliderect(platform.down_rect):
            self.direction[0] *= -1
            self.direction[1] = 1.0

        if self.rect.y <= 0 or self.rect.colliderect(platform.rect):
            self.direction[1] *= -1

        for i in range(len(bricks)):
            if self.rect.colliderect(bricks[i].rect):

                brick_collider = bricks[i].which_side_collides(self.rect)
                if brick_collider % 2 == 0:
                    self.direction[1] *= -1
                else:
                    self.direction[0] *= -1

                if bricks[i].take_shot():
                    if bricks[i].has_drop:  # brick[i] got destroyed
                        drop_object = Drop.Drop(bricks[i].drop)
                        drop_object.start_falling(bricks[i].phantom_rect)
                        drops.append(drop_object)
                    bricks.pop(i)

                break

        self.rect.x += self.velocity * self.direction[0]
        self.rect.y += self.velocity * self.direction[1]

        self.update_rotation(dt)