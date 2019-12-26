""" 14-2 练习的子弹管理 """
import pygame
from pygame.sprite import Sprite
from random import randint

class Myrect(Sprite):
    """ 矩形 """
    def __init__(self,screen,myset):
        # 
        super().__init__()
        self.screen= screen
        self.myset= myset
        self.screen_rect = screen.get_rect()
        self.left = self.screen_rect.width - 2* myset.myrect_width 
        self.rect =pygame.Rect(0,0,myset.myrect_width,myset.myrect_height)
        self.rect.x = self.rect.width + randint(0,self.left)
        if myset.myrect_direction == -1:
            # 通过方向判断方块生成的位置
            self.rect.y = self.screen_rect.height-myset.myrect_height
        else:
            self.rect.y = 0
        # print(myset.myrect_direction)
        # print(self.rect)
        self.y = float(self.rect.y)


    def update(self):
        # 移动时使用
        self.y +=self.myset.myrect_speed *self.myset.myrect_direction
        self.rect.y = self.y
    
    def draw_rect(self):
        pygame.draw.rect(self.screen, (255,0,0), self.rect)

    
    def check_edges(self):
        """ 检查是否碰到屏幕 """
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
        else:
            return False


