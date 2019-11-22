""" 入口 """
import pygame
from mysetting import Mysetting
# from my_funs import check_events
import my_funs as gf
# from pygame.color import THECOLORS
from hahas import Hahas
# 初始化屏幕


def paint_game():
    """ 主程序 """
    pygame.init()
    mys = Mysetting()
    screen = pygame.display.set_mode((mys.screen_w, mys.screen_h))
    # title='blue sola'

    haha = Hahas(screen, mys)
    pygame.display.set_caption(mys.titles)

    # bg_col=(0,0,255)

    while True:
        # 监视键盘鼠标事件
        gf.check_events(haha)
        haha.moveme()
        gf.update_screen(mys, screen, haha)

paint_game()
