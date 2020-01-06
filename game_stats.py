import json

class GameStats():
    """跟踪游戏的统计信息  """

    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏开始处于非活动状态
        self.game_active = False
        # self.high_score = 0
        

    def read_high_scroe(self):
        """ 读取最高分 """
        self.high_score = 0
        with open(self.ai_settings.file_name) as f_obj:
            high_score = json.load(f_obj)
        self.high_score= int(high_score)

    def reset_stats(self):
        """ 初始化在游戏运行时可能变化的统计信息  """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.read_high_scroe()