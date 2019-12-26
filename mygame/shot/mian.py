""" 14-2 练习的子弹管理 """
import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.append(o_path+"/mygame")
from mysetting import Mysetting 
import pygame
from pygame.sprite import Group
# from mygame.shiphh import Shiphh
from shot.ship import Ship
#from mygame.shot.button import Button
from shot.button import Button
#from mygame.shot.gamestat import GameStat
from shot.gamestat import GameStat
#import mygame.shot.shot_function as shot
import shot.shot_function as shot

def method():
    pygame.init()
    myset= Mysetting()
    screen = pygame.display.set_mode((myset.screen_w,myset.screen_h))
    pygame.display.set_caption(myset.shot_caption)
    
    stats = GameStat(myset)
    myrects = Group()
    ship= Ship(screen,myset)
    bullets = Group()
    play_button= Button(myset,screen, "开始")
    shot.create_rect(myrects, screen, myset)

    while True:
        shot.check_events(myset, screen, ship, bullets, stats, myrects, play_button)
        if stats.game_active:
            ship.moveme()
            shot.update_bullets(bullets,myset, screen, ship, myrects)
            shot.update_myrect(myset,myrects,ship,stats,screen,bullets)
        
        shot.update_screen(myset, screen,ship, bullets, myrects,play_button,stats)

method()           
