''' 船 '''
import pygame
# from settings import Settings
from pygame.sprite import Sprite 

class Ship(Sprite):
    ''' chushihua  '''

    def __init__(self, ai_settings, screen):
        ''' 初始化飞船，并设置其位置 '''
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)
        # 移动标志
        self.move_right = False
        self.move_left = False

    def blitme(self):
        '''  指定位置绘制飞船 '''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''# 根据移动标志调整位置 '''
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += float(self.ai_settings.ship_speed_factor)
            # self.center += float(self.ai_settings)
        if self.move_left and self.rect.left > 0:
            # self.rect.centerx += -1
            self.center -= float(self.ai_settings.ship_speed_factor)
        # 根据center 更新rec.centerx
        self.rect.centerx = self.center

    def center_ship(self):
        """ 让飞船居中 """
        self.center = self.screen_rect.centerx