"""  13-5 打球 13-6结束游戏"""
import pygame
from pygame.sprite import Group
from mysetting import Mysetting
from slab import Slab
import slab_ball_function as sbf
from slabballstats import SlabballStats

def run_game():
    """  入口程序 """
    pygame.init()
    myset = Mysetting()
    screen = pygame.display.set_mode((myset.screen_w, myset.screen_h))
    pygame.display.set_caption('play slab')

    stats = SlabballStats(myset)
    slab = Slab(myset, screen)

    balls = Group()
    sbf.create_ball(balls, screen, myset)

    while True:
        sbf.check_events(slab)
        if stats.game_active:
            sbf.slap_ball_update(slab, balls, screen, myset)
            sbf.update_balls(myset, balls, screen, stats)
        sbf.update_screen(myset, screen, balls, slab)


run_game()
