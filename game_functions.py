''' 管理事件 '''
import sys
import pygame
import json
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb):
    """ 相应按键 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        write_numbers(stats, ai_settings)
        sys.exit()
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(stats, aliens,bullets, ai_settings,screen,ship,sb)

def check_keyup_events(event, ship):
    """ 相应松开按键 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def start_game(stats, aliens, bullets, ai_settings, screen, ship,sb):
    # 开始或重制游戏操作
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    sb.prep_score()
    sb.prep_level()
    sb.pfep_ships()
    # sb.show_score()
    stats.game_active = True
    # 清空外星人和子弹
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens,
                      bullets, ship, ai_settings, screen, sb):
    """ 检查鼠标位置是否在按钮的rect选区里 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initializedynamic_settings()
        start_game(stats, aliens, bullets, ai_settings, screen, ship,sb)

def write_numbers(stats,ai_settings):
    """ 保存最高分 """
    with open(ai_settings.file_name,'w') as f_obj:
        json.dump(stats.high_score, f_obj)
        print("保存最高分"+str(stats.high_score))
   

def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens,sb):
    ''' 退出事件 '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_numbers(stats,ai_settings)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x,
                              mouse_y, aliens, bullets, ship, ai_settings, screen, sb)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets,stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb):
    ''' 更新屏幕，放上去'''
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_buller()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
     # 更新屏幕可见
    pygame.display.flip()

def check_high_score(stats, sb):
    """ 检查是否诞生最高分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """ 子弹击中外星人后消失，加快游戏节奏，并生成新的外星人 """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_score * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens, ship)


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """ 更新子弹位置，并删除已消失的子弹 """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)


def fire_bullets(bullets, ai_settings, screen, ship):
    """ 如果没有达到上限，发射一枚子弹 """
    if len(bullets) < ai_settings.bullet_allowed:
             # 创建子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取相应的措施 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ 将整理外星人下移，并改变他们的方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """ 相应外星人被撞到飞船 """
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # 更新余下飞船图片
        sb.pfep_ships()
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb):
    """ 检查是否有外星人达到地步，处理和外星人撞到飞船一样 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb):
    # 更新外星人群
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens, collided=None):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb)


def get_number_aliens_x(ai_settings, alien_width):
    # 计算外星人每行个数
    availabel_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(availabel_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    # 计算外星人每列个数
    availabel_space_y = ai_settings.screen_height - 2 * alien_height - ship_height
    number_aliens_y = int(availabel_space_y / (2 * alien_height))
    return number_aliens_y


def create_alien(aliens, screen, ai_settings, alien_number_x, row_number):
    # 创建单个外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number_x
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    # 创建外星人群
    alien = Alien(ai_settings, screen)
    # alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_number = get_number_aliens_y(
        ai_settings, ship.rect.height, alien.rect.height)
    # available_space_x = ai_settings.screen_width - 2 * alien_width
    # number_aliens_x = int(available_space_x /(2 * alien_width))
    for alien_number_y in range(row_number):
        for alien_number_x in range(number_aliens_x):
            create_alien(aliens, screen, ai_settings,
                         alien_number_x, alien_number_y)
        # alien = Alien(ai_settings, screen)
        # alien.x = alien_width + 2 * alien_width * alien_number
        # alien.rect.x = alien.x
        # aliens.add(alien)
