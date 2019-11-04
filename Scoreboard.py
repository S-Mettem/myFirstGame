"""
    Class Scoreboard
        Need to show score players

"""
import pygame.font


class Scoreboard:
    """Initialization class"""

    def __init__(self, screen, player, position_x, position_y):
        # Initialization parameters
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.player = player

        # set caption
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48, italic=True)

        # Preparation image to print on screen
        self.prep_img()

    def prep_img(self):
        """Convert current score to graphic image"""
        # Convert integer score to string type
        score_str = str(self.player.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Place score to position
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.position_x
        self.score_rect.centery = self.position_y

    def show_score(self):
        """Show scoreboard"""
        self.screen.blit(self.score_image, self.score_rect)
