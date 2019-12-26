""" 14-2 练习的子弹管理 """
class GameStat():
    """ 游戏管理 """
    def __init__(self, myset):
        """ 初始化 """
        self.myset = myset
        self.reset_stats()

        self.game_active= False

    def reset_stats(self):
        self.ship_left = self.myset.ship_limit