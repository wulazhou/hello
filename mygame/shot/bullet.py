""" 14-2 练习的子弹管理 """
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ 子弹管理 """
    def __init__(self, myset, screen, ship):
        """ 继承父类 初始化子弹的位置，颜色，速度 """
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, myset.bullet_width, myset.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        self.x = float(self.rect.x)

        self.color = myset.bullet_color
        self.speed = myset.bullet_speed

    def update(self):
        #移动子弹
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        # 画子弹
        pygame.draw.rect(self.screen, self.color, self.rect)