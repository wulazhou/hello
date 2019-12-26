""" 14-2 练习的子弹管理 """
import pygame
import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)
#from mygame.ship_bullet import Bullet
from shot.bullet import Bullet
#from mygame.shot.myrect import Myrect
from shot.myrect import Myrect
#import mygame.new_funs as newfuns
import new_funs as newfuns
from time import sleep

def check_events(myset,screen,ship,bullets,stats,myrects,play_button):
    """ 事件管理 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            check_play_button(stats, myrects, play_button, bullets, ship, myset, screen,mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, myset, screen, ship, bullets, stats, myrects)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_play_button(stats, myrects, play_button, bullets, ship, myset, screen, mouse_x, mouse_y):
    """ 开始按钮设置 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(stats, myrects, bullets, myset, screen, ship)

def start_game(stats, myrects, bullets, myset, screen, ship):
    """ 开始重制处理的相关 """
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active= True

    myrects.empty()
    bullets.empty()
    create_rect(myrects,screen,myset)
    ship.center_ship()
    


def check_keydown_events(event,myset, screen, ship, bullets,stats,myrects):
    """ 按住按钮时处理 """
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, myset, screen, ship)

def check_keyup_events(event, ship):
    """ 放开按钮时处理 """
    if event.key == pygame.K_DOWN:
        ship.move_down= False
    elif event.key == pygame.K_UP:
        ship.move_up = False

def fire_bullet(bullets, myset, screen, ship):
    # 限制子弹个数
    if len(bullets) < myset.bullet_allwed:
        new_bullet = Bullet(myset, screen, ship)
        bullets.add(new_bullet)

def create_rect(myrects, screen, myset):
    # 产生方块
    myrect = Myrect(screen, myset)
    myrects.add(myrect)

def update_bullets(bullets, mys, screen, ship, myrects):
    """ 子弹控制管理 超出边界 就减少"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= mys.screen_w:
            bullets.remove(bullet)
        # print(len(bullets))
    check_bullet_myrect_collisions(mys, screen, ship, myrects, bullets)

def check_bullet_myrect_collisions(myset, screen, ship, myrects, bullets):
    """ 子弹击中方块后，方块消失并生成新的方块 """
    collsiions = pygame.sprite.groupcollide(bullets, myrects, True, True)
    if len(myrects) == 0:
        change_rect_direction(myset)
        bullets.empty()
        create_rect(myrects, screen, myset)
        # print("1change direction ")
        # print(myset.myrect_direction)

def update_myrect(myset, myrects, ship, stats, screen, bullets):
    """ 更新方块 """
    myrects.update()
    isRemveRect = False
    
    for myrect in myrects.sprites():
        if myrect.check_edges():
            # print("2-------------"+str(len(myrects)))
            # print(myrect.rect)
            # print(myrect.screen_rect)
            isRemveRect = True
            break
    
    if isRemveRect:
        # print("2-------------shot")
        ship_shot(myset,stats,screen,ship, myrects,bullets)

def change_rect_direction(myset):
    """改变方块方向  """
    myset.myrect_direction *= -1
    # print("change------------- "+str(myset.myrect_direction))

def ship_shot(myset,stats, screen, ship, myrects, bullets):
    """ 方块碰到边缘 没有被击中 """
    if stats.ship_left >0:
        # print("3ship_shot "+str(myset.myrect_direction))
        stats.ship_left -= 1
        myrects.empty()
        change_rect_direction(myset)
        create_rect(myrects, screen, myset)
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_screen(myset, screen, ship, bullets, myrects,play_button, stats):
    """ 更新屏幕上的图片，切换到新屏幕 """
    screen.fill(myset.bg_col)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.biteme()
    for myrect in myrects.sprites():
        myrect.draw_rect()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
