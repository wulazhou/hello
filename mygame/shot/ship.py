""" 引入 pygame 类 """
import pygame


class Ship():
    # 初始化
    def __init__(self, screen, myset):
        self.myset = myset
        self.screen = screen
        self.image = pygame.image.load(myset.ship_image_wloc)
        self.screen_rec = screen.get_rect()
        self.rect = self.image.get_rect()
        # 飞船方左侧中央
        self.rect.centery = self.screen_rec.centery
        self.rect.left = self.screen_rec.left

        # 飞船上下移动标志
        self.move_up = False
        self.move_down = False
        self.rect_centery = self.rect.centery

    def biteme(self):
        """ 在图上放置image """
        self.screen.blit(self.image, self.rect)

    def moveme(self):
        # 移动飞船
        if self.move_up and self.rect.top > 0:
            self.rect_centery -= self.myset.ship_speed
        elif self.move_down and self.rect.bottom < self.screen_rec.bottom:
            self.rect_centery += self.myset.ship_speed
        # 更新飞船y 坐标
        self.rect.centery = self.rect_centery

    def center_ship(self):
        """ 让飞船居中 """
        self.rect_centery= self.screen_rec.centery




