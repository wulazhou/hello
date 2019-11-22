import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):
    """ 球管理类 """

    def __init__(self, myset, screen):
        super().__init__()
        self.screen = screen
        self.screen_rec = screen.get_rect()
        self.myset = myset
        self.rect = pygame.Rect(
            0, 0, myset.ball_rect_width, myset.ball_rect_height)
        self.rect.centerx = myset.ball_radius + randint(0,
                                                        myset.screen_w-myset.ball_rect_width)
        # self.rect.centerx = 1550
        self.rect.top = self.screen_rec.top
        self.y = float(self.rect.centery)
        self.color = myset.ball_color
        self.speed_factor = 3

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.rect.centerx, self.rect.centery),
                           self.myset.ball_radius)

    def check_edges(self):
        """ 检查是否遇到屏幕 """
        if self.rect.bottom >= self.screen_rec.bottom:
            return True
        else:
            return False
