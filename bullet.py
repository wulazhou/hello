import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ 子弹管理类 """

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_heigth)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y =self.y

    def draw_buller(self):
        pygame.draw.rect(self.screen, self.color, self.rect)