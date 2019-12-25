class Mysetting():
    def __init__(self):
        self.bg_col = (22, 73, 157)
        self.screen_h = 900
        self.screen_w = 1600
        self.titles = 'blue solar'
        self.ship_speed = 2.0
        self.ship_bg_col =230, 230, 230
        self.haha_speed = 2.0 
        # 速度
        self.haha_image_loc = 'lan.jpg' 
        self.ship_image_loc = 'shiphh.jpg' 
        # 地址
        self.bullet_speed = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 255, 51, 0
        self.bullet_allwed = 4

        # 星星
        self.star_image_loc = 'xinxin/xinxin25.bmp'

        # 雨滴
        self.raindrop_image_loc = 'yudi.jpg'
        self.raindrop_speed = 5

        # 定义球 13.5-13.6
        self.ball_color = (215, 194, 0)
        self.ball_radius = 75
        self.ball_rect_width = 150
        self.ball_rect_height = 150

        # 定义平板 
        self.slab_width = 150
        self.slab_height = 30
        self.slab_color = 255, 51, 0
        self.slab_speed = 10
        self.slab_limit = 3


        # 14-2按钮
        self.button_text= "按钮"
        self.ship_limit = 3
        self.ship_image_wloc = 'mygame/shiphh.jpg'
        self.shot_caption= "14-2 射击练习"
        self.button_width=200
        self.button_height=50
        self.button_text_color = (255, 255, 255)
        self.button_color =(0, 0, 255)
        self.button_font_size =48
        self.myrect_width = 100
        self.myrect_height = 100
        self.myrect_speed = 5
        # 方块移动方向 1 下，-1 上
        self.myrect_direction =1
        


