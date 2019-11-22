
""" 练习12-5入口 向右发射子弹 """
import pygame
from pygame.sprite import Group
from shiphh import Shiphh
import new_funs as gf
from mysetting import Mysetting


def new_paint():
    # 入口
    pygame.init()
    mys = Mysetting()
    screen = pygame.display.set_mode((mys.screen_w, mys.screen_h))
    pygame.display.set_caption(mys.titles)
    ship = Shiphh(screen, mys)
    bullets = Group()

    while True:
        gf.check_events(mys, ship, bullets, screen)
        ship.moveme()
        gf.update_bullets(bullets,mys)
        gf.update_screen(mys, screen, ship, bullets)

new_paint()