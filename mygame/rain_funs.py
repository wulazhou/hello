""" 事件管理类 """
import sys
import pygame
from raindrop import Raindrop


def check_events():
    """ 监听屏幕事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(myset, screen, raindrops):
    """ 屏幕上色，雨滴更新，屏幕更新 """
    screen.fill(myset.bg_col)
    raindrops.draw(screen)
    # raindrops.blitme()
    pygame.display.flip()


def update_raindops(myset, raindrops, screen):
    """ 移动雨滴 """
    # print(raindrops.__len__())
    rain_len = raindrops.__len__()
    check_fleet_edges(raindrops)
    if raindrops.__len__() < rain_len:
        creatd_fleet(myset, screen, raindrops, False)
        # raindrop = Raindrop(screen, myset)
        # rain_width = raindrop.rect.width
        # x_number = get_raindrop_x_number(rain_width, myset)
        # for x in range(x_number):
        #     create_raindrop(screen, myset, raindrops, x, 0)

    raindrops.update()


def check_fleet_edges(raindrops):
    """检查雨滴群是否掉出屏幕 """
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrops.remove(raindrop)


def create_raindrop(screen, myset, raindrops, x_number, y_number):
    """ 创建单个雨滴 """
    raindrop = Raindrop(screen, myset)
    h = raindrop.rect.height
    w = raindrop.rect.width
    raindrop.rect.x = w + 2 * x_number * w
    raindrop.x = raindrop.rect.x
    raindrop.rect.y = h + 2 * y_number * h
    raindrop.y = raindrop.rect.y
    raindrops.add(raindrop)


def creatd_fleet(myset, screen, raindrops, noline=True):
    """ 创建雨滴群 默认生成全屏雨滴，如果noline = false， 则生成一行雨滴 """
    raindrop = Raindrop(screen, myset)
    rain_width = raindrop.rect.width
    rain_height = raindrop.rect.height
    x_number = get_raindrop_x_number(rain_width, myset)
    if noline:
        y_number = get_raindrop_y_number(rain_height, myset)
    else:
        y_number = 1

    for y in range(y_number):
        for x in range(x_number):
            create_raindrop(screen, myset, raindrops, x, y)


def get_raindrop_x_number(rain_width, myset):
    """ 计算一行有几个雨滴 """
    middle_screen = myset.screen_w - (2*rain_width)
    x_number = int(middle_screen / (2*rain_width))
    return x_number


def get_raindrop_y_number(rain_height, myset):
    """ 计算可以有几行雨滴 """
    middle_h_screen = myset.screen_h - (2 * rain_height)
    y_number = int(middle_h_screen / (2 * rain_height))
    return y_number
