import pygame
import Screen

IMAGES = [pygame.image.load('assets/the_powerup_laser.png'), pygame.image.load('assets/the_powerup_length.png'),
          pygame.image.load('assets/the_powerup_3balls.png'), pygame.image.load('assets/the_downgrade_length.png')]
# DROP1_IMAGE = pygame.image.load('assets/the_powerup_length.png')
# DROP2_IMAGE = pygame.image.load('assets/the_powerup_3balls.png')
# DROP3_IMAGE = pygame.image.load('assets/the_downgrade_length.png')

SIZE_X = 32
SIZE_Y = 32
STARTING_POSITION = (0,0)
VELOCITY = 3


class Drop:
    def __init__(self, which = 0, x = STARTING_POSITION[0], y = STARTING_POSITION[1]):
        self.rect = pygame.Rect(x,y,SIZE_X,SIZE_Y)
        self.which = which
        self.image = pygame.transform.scale(IMAGES[which], (SIZE_X, SIZE_Y))
        self.falling = False
        self.velocity = VELOCITY




    def start_falling(self, brick_rect):
        self.rect.center = brick_rect.center
        self.falling = True



    def draw(self, WINDOW):
        if self.falling:
            WINDOW.blit(self.image, self.rect)

    def update(self, platform_rect):
        if not self.falling:
            return None

        self.rect.y += self.velocity

        if self.rect.colliderect(platform_rect):
            self.falling = False# destory
            return self.which

        if self.rect.y >= Screen.HEIGHT:
            self.falling = False# destory
            return -1







