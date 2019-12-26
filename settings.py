''' 初始化  '''
class Settings():
    '''  初始化 '''
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的速度
        # self.ship_speed_factor = 2
        self.ship_limit = 3
        # self.bullet_speed_factor = 3
        # 子弹的速度
        self.bullet_width = 3
        self.bullet_heigth = 15
        # 子弹长宽
        self.bullet_color = 109, 109, 109
        # 子弹的颜色
        self.bullet_allowed = 3

        # 外星人地址
        self.alien_loc = 'images/alien.bmp'
        # 外星人速度
        # self.allen_speed_factor = 3
        self.fleet_drop_speed = 10
        # 外星人移动方向 1 右，-1 左
        # self.fleet_direction = 1
        #游戏速度节奏
        self.speedup_scale = 1.1
        self.initializedynamic_settings()

    def initializedynamic_settings(self):
        """ 初始化游戏随进行而变化的设置 """
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.allen_speed_factor = 2
        # 外星人移动方向 1 右，-1 左
        self.fleet_direction = 1
    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.allen_speed_factor *= self.speedup_scale
