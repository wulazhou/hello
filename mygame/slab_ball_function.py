""" 管理事件 """
import sys
import pygame
from ball import Ball
from time import sleep
# from slab import Slab

def check_keydown_events(event, slab):
    """ 相应按键，修改移动标志位 """
    if event.key == pygame.K_RIGHT:
        slab.move_right = True
    elif event.key == pygame.K_LEFT:
        slab.move_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, slab):
    """ 松开按键，修改移动标志位 """
    if event.key == pygame.K_RIGHT:
        slab.move_right = False
    elif event.key == pygame.K_LEFT:
        slab.move_left = False

def check_events(slab):
    """ 监听事件，作出相应的处理方向 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, slab)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, slab)

def update_screen(myset, screen, balls, slab):
    """ 更新屏幕 """
    screen.fill(myset.bg_col)
    slab.draw_slab()
    for ball in balls.sprites():
        ball.draw_ball()
    pygame.display.flip()

def check_slab_ball_collisions(myset, screen, balls, slab):
    """ 球板与球碰撞后删除球，产生新的球 """
    collisions = pygame.sprite.spritecollide(slab, balls, True)
    if len(balls)== 0:
        create_ball(balls,screen, myset)

def slap_ball_update(slap, balls, screen, myset):
    """  """
    slap.update()
    check_slab_ball_collisions(myset, screen, balls, slap)

def create_ball(balls, screen, myset):
    """ 随机产生球 """
    ball = Ball(myset, screen)
    balls.add(ball)

def ball_hit(balls, screen, myset,stats):
    """ 球碰到底部 """
    if stats.slab_left > 0:
        balls.empty()
        create_ball(balls, screen, myset)
        stats.slab_left -= 1
        sleep(0.5)
    else:
        stats.game_active = False

def check_balls_edge(balls):
    """ 检查球是否碰到底部 """
    for ball in balls.sprites():
        if ball.check_edges():
            return True
        break

def update_balls(myset, balls, screen, stats):
    """ 更新球 """
    balls.update()
    isremove = False

    for ball in balls.sprites():
        if ball.check_edges():
            isremove = True
            break

    if isremove:
        ball_hit(balls, screen, myset, stats)
        # balls.empty()
        # create_ball(balls,screen,myset)  
        # if stats.slab_left > 0:
        #     stats.slab_left -= 1
        #     sleep(0.5)
        # else:
        #     stats.game_active = False