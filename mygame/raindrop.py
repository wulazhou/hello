""" 创建雨滴  """
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, screen, myset):
        super().__init__()
        self.screen = screen
        self.myset = myset

        self.image = pygame.image.load(myset.raindrop_image_loc)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # 在指定位置放雨滴
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ 检查雨滴是否掉出屏幕 """
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """ 向下移动 """
        self.y += self.myset.raindrop_speed
        self.rect.y = self.y
