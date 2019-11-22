class SlabballStats():
    """ 跟踪游戏的统计信息 """
    def __init__(self, myset):
        """ 初始化统计信息 """
        self.myset = myset
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """ 初始化游戏运行期间可能变化的统计信息 """
        self.slab_left = self.myset.slab_limit