""" 引入 pygame 类 """
import pygame

#  位图类
class Hahas():
    # 初始化位图
    def __init__(self, screen, mysets):
        self.mysets = mysets
        self.screen = screen
        self.image = pygame.image.load(mysets.haha_image_loc)
        self.rect = self.image.get_rect()  #图像坐标
        self.screen_rect = screen.get_rect()  #屏幕坐标
        self.rect.centerx = self.screen_rect.centerx  # 横坐标
        self.rect.centery = self.screen_rect.centery  # 纵坐标
        # 决定是否移动标志位
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.rect_centerx = float(self.rect.centerx)
        self.rect_centery = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ 指定位置放位图 """
        self.screen.blit(self.image, self.rect)

    def moveme(self):
        """ 根据标志位，决定往哪移动 """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect_centerx += self.mysets.haha_speed
        elif self.move_left and self.rect.left > 0:
            self.rect_centerx -= self.mysets.haha_speed
        elif self.move_up and self.rect.top > 0:
            self.rect_centery -= self.mysets.haha_speed
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect_centery += self.mysets.haha_speed

        self.rect.centerx = self.rect_centerx
        self.rect.centery = self.rect_centery
