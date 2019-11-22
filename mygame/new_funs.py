import pygame
import sys
from ship_bullet import Bullet


def check_keyup_events(event, ship):
    """ 放掉按键 """
    if event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def check_keydown_evnets(event, ship, myset, screen, bullets):
        # 按住按键
    if event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, myset, screen, ship)
        # if len(bullets) < myset.bullet_allwed: #限制子弹个数
        #     new_bullet = Bullet(myset, screen, ship)
        #     bullets.add(new_bullet)


def check_events(myset, ship, bullet, screen):
    # 所有事件检查方法
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_evnets(event, ship, myset, screen, bullet)


def update_screen(ai_setting, screen, ship, bullets):
    """ 更新屏幕上的图片，切换到新屏幕 """
    screen.fill(ai_setting.bg_col)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.biteme()
    pygame.display.flip()


def update_bullets(bullets, mys):
    """ 子弹控制管理 超出边界 就减少"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= mys.screen_w:
            bullets.remove(bullet)
        # print(len(bullets))


def fire_bullet(bullets, myset, screen, ship):
    # 限制子弹个数
    if len(bullets) < myset.bullet_allwed:
        new_bullet = Bullet(myset, screen, ship)
        bullets.add(new_bullet)
