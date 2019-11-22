""" 事件管理类 """
import sys
import pygame
from star import Star
from random import shuffle, randint

def check_events():
    """ 检查事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(myset, screen, stars):
    """ 更新屏幕 """
    screen.fill(myset.bg_col)
    stars.draw(screen)
    pygame.display.flip()


def get_number_star_x(myset, star_width):
    # 计算一行星星 可以装多少个
    avai_x = myset.screen_w - 2 * star_width
    number_star_x = int(avai_x/(2*star_width))
    return number_star_x


def get_rowno_star(myset, star_height):
    # 计算屏幕又多少列星星
    avai_y = myset.screen_h - 3 * star_height
    number_star_y = int(avai_y / (2 * star_height))
    return number_star_y


def creat_star(myset, screen, stars, number_y, number_x):
    # 根据坐标画星星
    star = Star(myset, screen)
    star_width = star.rect.width
    star.x = randint(-11, 11) + 2 * star_width * number_x
    star.rect.x = star.x
    star.rect.y = randint(-11,11) + 2 * star.rect.height * number_y
    # print(star.rect, end='\t')
    stars.add(star)


def create_fleet(myset, screen, stars):
    # 创建星星群
    star = Star(myset, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    row_no = get_rowno_star(myset, star_height)
    line_no = get_number_star_x(myset, star_width)

    """ for number_y in range(row_no):
        for number_x in range(line_no):
            creat_star(myset, screen, stars, number_y, number_x) """

    for number_y in range(row_no):
        for number_x in range(line_no):
            creat_star(myset, screen, stars, number_y, number_x)