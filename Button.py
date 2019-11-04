"""
    Button class


"""
import pygame.font


class Button:
    def __init__(self, screen, width, height, position_x, position_y,
                 text, font_size, bg_color=(107, 209, 52), text_color=(0, 0, 0),
                 bold=False, italic=False):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # initialization main settings
        self.width, self.height = width, height
        self.text_color = text_color
        self.bg_color = bg_color
        self.text = text
        self.size = font_size
        self.font = pygame.font.SysFont(None, self.size, bold, italic)

        # Create a class and position at the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = position_x
        self.rect.centery = position_y
        self.prep_msg()

    def prep_msg(self):
        self.text_image = self.font.render(self.text, True, self.text_color,
                                           self.bg_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
