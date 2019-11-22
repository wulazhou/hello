import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self, ai_settings, screen):
        # 初始化外星人的起始位置，坐标x，坐标y
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(ai_settings.alien_loc)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 每次更新屏幕时，外星人向右移动
        self.x += (self.ai_settings.allen_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """ 如果外星人位于屏幕边缘，返回true """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True