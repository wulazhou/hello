""" 练习13-1画星星 """
import pygame
from pygame.sprite import Group
from mysetting import Mysetting
import star_funs as gf


def paint_star_screen():
    """ 主程序 """
    pygame.init()
    mys = Mysetting()
    screen = pygame.display.set_mode((mys.screen_w, mys.screen_h))
    pygame.display.set_caption(mys.titles)
    
    stars = Group()
    gf.create_fleet(mys, screen, stars)
    while True:
        gf.check_events()
        gf.update_screen(mys, screen, stars)


paint_star_screen()
