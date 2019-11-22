""" 事件声明 """
import sys
import pygame
# 事件声明


def check_keyup_events(event, haha):
    """ 按键放下事件 """
    if event.key == pygame.K_LEFT:
        haha.move_left = False
    elif event.key == pygame.K_RIGHT:
        haha.move_right = False
    elif event.key == pygame.K_UP:
        haha.move_up = False
    elif event.key == pygame.K_DOWN:
        haha.move_down = False

def check_keydown_events(event,haha):
    """ 按键不放事件 """
    if event.key == pygame.K_LEFT:
        haha.move_left = True
    elif event.key == pygame.K_RIGHT:
        haha.move_right = True
    elif event.key == pygame.K_UP:
        haha.move_up = True
    elif event.key == pygame.K_DOWN:
        haha.move_down = True 

def check_events(haha):
    """ 所有事件检查入口 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,haha)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, haha)


def update_screen(mysets, screen, haha):
    """ 更新屏幕内容，并切换到新屏幕 """
    screen.fill(mysets.bg_col)
    # 让最近的绘制屏幕可见
    haha.blitme()
    # haha.bgcolor(mys.bg_col)
    pygame.display.flip()
    # 重绘屏幕背景色
