import pygame
import Drop

LASER_IMAGE = pygame.image.load('assets/the_laser.png')
STARTING_POSITION = (0, 0)
VELOCITY = 7
SIZE_X = 8
SIZE_Y = 16

class Laser:
    def __init__(self, x = STARTING_POSITION[0], y = STARTING_POSITION[1]):
        self.rect = pygame.Rect(x, y, SIZE_X, SIZE_Y)
        self.image = pygame.transform.scale(LASER_IMAGE, (SIZE_X, SIZE_Y))
        self.velocity = VELOCITY
        self.active = False

    def destroy(self):
        self.rect.x = (-1)*self.rect.width
        self.rect.y = (-1)*self.rect.height
        self.active = False

    def update(self, bricks, drops):
        if not self.active:
            return None

        self.rect.y -= self.velocity

        for i, brick in enumerate(bricks):
            if self.rect.colliderect(brick.rect):
                self.destroy()
                if bricks[i].take_shot():
                    if bricks[i].has_drop:  # brick[i] got destroyed
                        drop_object = Drop.Drop(bricks[i].drop)
                        drop_object.start_falling(bricks[i].phantom_rect)
                        drops.append(drop_object)
                    bricks.pop(i)


        if self.rect.y <= -1*self.rect.height:
            self.destroy()



    def shoot(self, platform_rect):
        self.rect.center = platform_rect.center
        self.rect.y += platform_rect.height//2
        self.active = True



    def draw(self, WINDOW):
        if not self.active:
            return None
        WINDOW.blit(self.image, self.rect)