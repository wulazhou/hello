'''  外星人 '''
# import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
    '''   初始化   '''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人打飞船")

    stats = GameStats(ai_settings)
    # 创建一飞船
    ship = Ship(ai_settings, screen)
    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # alien = Alien(ai_settings, screen)
    # bg_color = (0, 255, 0)
    # 创建子弹
    bullets = Group()
    while True:
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()

            # bullets.update()
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            gf.update_bullets(ai_settings,screen,ship,aliens, bullets)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
            # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()


run_game()
