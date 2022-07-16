import pygame
import random

BRICK_IMAGE_GREEN = pygame.image.load('assets/the_green_brick.png')
BRICK_IMAGE_PURPLE = pygame.image.load('assets/the_purple_brick.png')
BRICK_IMAGE_GREY = pygame.image.load('assets/the_grey_brick.png')
BRICK_IMAGE_ORANGE = pygame.image.load('assets/the_orange_brick.png')
BRICK_IMAGE_BLUE = pygame.image.load('assets/the_blue_brick.png')
BRICK_SIZE_X = 48
BRICK_SIZE_Y = 16
BRICK = pygame.transform.scale(BRICK_IMAGE_GREEN, (BRICK_SIZE_X, BRICK_SIZE_Y))
BRICK_STARTING_POSITION = (0, 0)
BASIC_BRICK_HP = 1
DESTROYED = False
ALIVE = True
SIDE_RECT_COLLIDER_X = BRICK_SIZE_X //8
SIDE_RECT_COLLIDER_Y = BRICK_SIZE_Y//3
DROP_RATE = 500
AMOUNT_OF_DROP = 4



class Brick:

    def __init__(self, x = BRICK_STARTING_POSITION[0], y = BRICK_STARTING_POSITION[1], hit_points = BASIC_BRICK_HP, brick_size = (BRICK_SIZE_X, BRICK_SIZE_Y),
                 drop_rate = DROP_RATE):
        self.rect = pygame.Rect(x, y, brick_size[0], brick_size[1])
        self.hit_points = hit_points
        self.has_drop = self.set_drop(drop_rate)
        self.drop = -1
        if self.has_drop:
            self.drop = random.randint(0,AMOUNT_OF_DROP - 1)
        self.update_image()
        self.phantom_rect = pygame.Rect(x,y, BRICK_SIZE_X, BRICK_SIZE_Y)


    def set_drop(self,drop_rate):
        rand = random.randint(1,100)
        if rand <= drop_rate:
            return True
        return False



    def update_image(self):
        if self.hit_points >= float('inf'):
            img = BRICK_IMAGE_GREY
        elif self.hit_points >= 4:
            img = BRICK_IMAGE_PURPLE
        elif self.hit_points == 3:
            img = BRICK_IMAGE_ORANGE
        elif self.hit_points == 2:
            img = BRICK_IMAGE_BLUE
        else:
            img = BRICK_IMAGE_GREEN

        self.image = pygame.transform.scale(img, (self.rect.width, self.rect.height))


    def draw(self,WINDOW):
        WINDOW.blit(self.image)

    def destroy(self):
        self.rect.x = (-1)*self.rect.width
        self.rect.y = (-1)*self.rect.height

    def take_shot(self):
        self.hit_points -= 1
        if self.hit_points == 0:
            self.destroy()
            return True
        else:
            self.update_image()
            return False


    def which_side_collides(self,rect_collider):
        side_rect_l = pygame.Rect(self.rect.x, self.rect.y + BRICK_SIZE_Y//3, SIDE_RECT_COLLIDER_X, SIDE_RECT_COLLIDER_Y)
        side_rect_r = pygame.Rect(self.rect.x + BRICK_SIZE_X - SIDE_RECT_COLLIDER_X, self.rect.y + BRICK_SIZE_Y//3,
                                  SIDE_RECT_COLLIDER_X,SIDE_RECT_COLLIDER_Y)



        if rect_collider.colliderect(side_rect_r) or rect_collider.colliderect(side_rect_l):
            return 1
        else:
            return 0
        
    
