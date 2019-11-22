import pygame
from pygame.sprite import Group
from mysetting import Mysetting
import rain_funs as rf
# from raindrop import Raindrop


def paint_rains():
    """ 入口程序 """
    pygame.init()
    myset = Mysetting()
    screen = pygame.display.set_mode((
        myset.screen_w, myset.screen_h))
    raindrops = Group()
    # 画雨群
    # raindrop = Raindrop(screen, myset)
    rf.creatd_fleet(myset, screen, raindrops)
    while True:
        rf.check_events()
        # rf.update_raindops(myset,screen,raindrops)
        rf.update_raindops(myset, raindrops, screen)
        # print(raindrops.__len__)
        rf.update_screen(myset, screen, raindrops)


paint_rains()
