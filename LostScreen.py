import pygame
import Screen

pygame.init()

BIG_FONT_SIZE = 64
SMALL_FONT_SIZE = 32
FONT_BIG = pygame.font.Font('assets/font.ttf', BIG_FONT_SIZE)
FONT_SMALL = pygame.font.Font('assets/font.ttf', SMALL_FONT_SIZE)
MAIN_TEXT_CENTER_POSITION = (Screen.WIDTH // 2, Screen.HEIGHT // 2)
OPTIONS_TEXT_CENTER_POSITION = (Screen.WIDTH // 2, 3*Screen.HEIGHT // 4)

POINTER_IMG = pygame.image.load('assets/the_pointer.png')
POINTER_SIZE_X = 16
POINTER_SIZE_Y = 16
WAITING_TIME = 300


class Scene:
    def __init__(self, text = None, options = None, color = (255, 255, 255), text_color = (0, 0, 0)):

        self.options = []
        self.bg_color = color
        self.text_color = text_color
        self.text = FONT_BIG.render(text, True, self.text_color, self.bg_color)

        self.main_rect = self.text.get_rect()
        self.main_rect.centerx = MAIN_TEXT_CENTER_POSITION[0]
        self.main_rect.centery = MAIN_TEXT_CENTER_POSITION[1]
        self.current_option = 0
        self.opt_rects = []


        for str in options:
            self.options.append(FONT_SMALL.render(str, True, self.text_color, self.bg_color))



        for i in range(len(self.options)):
            self.opt_rects.append(self.options[i].get_rect())
            self.opt_rects[i].centery = OPTIONS_TEXT_CENTER_POSITION[1]
            self.opt_rects[i].centerx = (i+1)*Screen.WIDTH//(len(options)+1)

        self.pointers = [Pointer(self.opt_rects[i]) for i in range(len(self.opt_rects))]
        if self.pointers[0]:
            self.pointers[0].change_state()


    def draw(self, WINDOW):
        WINDOW.fill(self.bg_color)
        WINDOW.blit(self.text, self.main_rect)
        for i, option in enumerate(self.options):
            WINDOW.blit(option,self.opt_rects[i])
            self.pointers[i].draw(WINDOW)

        pygame.display.update()

    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            self.pointers[self.current_option].change_state()
            self.current_option += len(self.options) - 1
            self.current_option %= len(self.options)
            self.pointers[self.current_option].change_state()
            pygame.time.wait(WAITING_TIME)
        if keys_pressed[pygame.K_d]:
            self.pointers[self.current_option].change_state()
            self.current_option += 1
            self.current_option %= len(self.options)
            self.pointers[self.current_option].change_state()
            pygame.time.wait(WAITING_TIME)
        if keys_pressed[pygame.K_SPACE]:
            return self.current_option
        return None




class Pointer:
    def __init__(self, rect_2_point):
        self.sizey = rect_2_point.height//2
        self.sizex = self.sizey

        self.rect_l = pygame.Rect(rect_2_point.x - self.sizex, rect_2_point.y + self.sizey//2, self.sizex, self.sizey)
        self.rect_r = pygame.Rect(rect_2_point.x + rect_2_point.width, rect_2_point.y + self.sizey//2, self.sizex, self.sizey)

        self.pointer_l = pygame.transform.scale(POINTER_IMG, (self.sizex, self.sizex))
        self.pointer_r = pygame.transform.scale(POINTER_IMG, (self.sizex, self.sizex))
        self.pointer_r = pygame.transform.rotate(self.pointer_r,180)
        self.active = False

    def draw(self, WINDOW):
        if not self.active:
            return
        WINDOW.blit(self.pointer_r, self.rect_r)
        WINDOW.blit(self.pointer_l, self.rect_l)

    def change_state(self):
        self.active = not self.active







