""" 创建星星  """
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, myset, screen):
        super().__init__()
        self.myset = myset
        self.screen = screen

        self.image = pygame.image.load(myset.star_image_loc)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        self.x = float(self.rect.x)
        
    def blitme(self):
        # 在指定位置放星星
        self.screen.blit(self.image, self.rect)