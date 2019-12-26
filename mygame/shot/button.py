import pygame.font
""" 14-2 练习的子弹管理 """
class Button():
    """ 创建按钮 """
    def __init__(self, myset, screen, msg):
        """ 初始化按钮 """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 按钮的尺寸，底色，字体大小，字体颜色
        self.width, self.height = myset.button_width, myset.button_height
        self.button_color = myset.button_color
        self.text_color = myset.button_text_color
        self.font = pygame.font.SysFont("stheitittf", myset.button_font_size, bold=False, italic=False)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """ 渲染文字成图像 """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center= self.rect.center
    
    def draw_button(self):
        # 填色
        self.screen.fill(self.button_color,self.rect)
        # 填文本
        self.screen.blit(self.msg_image,self.msg_image_rect)