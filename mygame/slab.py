import pygame
from pygame.sprite import Sprite


class Slab(Sprite):
    """ 球板 """

    def __init__(self, myset, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.myset = myset
        self.color = myset.slab_color
        self.rect = pygame.Rect(0, 0, myset.slab_width, myset.slab_height)
        self.rect.centerx = self.screen_rect.centerx  # 水平位置
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False

    def draw_slab(self):
        """ 绘制球板 """
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """ 根据标志位移动球板 """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += float(self.myset.slab_speed)
        if self.move_left and self.rect.left > 0:
            self.center -= float(self.myset.slab_speed)

        self.rect.centerx = self.center
