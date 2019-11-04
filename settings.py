"""
    Settings class
        There are stored all settings to
        screen, players, ball, static and dynamic settings
    Static settings - is settings,
        who don't change at the time of game
    Dynamic - is change at the time of game
"""
from random import randint, seed


class Settings:
    def __init__(self, screen_height, screen_width, name_screen):
        seed()
        # Settings for game
        # direction of ball at x cord
        self.roll_dice_x = 0
        # direction of ball at y cord
        self.roll_dice_y = 0
        # Assign that variables
        self.roll_dice()
        # Start or end of game
        self.game_active = False
        # Point to win one of players
        self.point_to_win = 1

        # Settings to main screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.window_name = name_screen

        # Settings to players
        self.player_height = 120
        self.player_width = 10
        self.player_speed = 2

        # Settings to ball
        self.ball_speed = 2
        self.ball_radius = 20

        # Settings to background

    def roll_dice(self):
        """Assign random numbers to roll_dice_x and
            roll_dice_y to direction ball"""
        tmp = randint(0, 1)
        if tmp == 0:
            self.roll_dice_x = -1
        else:
            self.roll_dice_x = 1

        tmp = randint(0, 1)
        if tmp == 0:
            self.roll_dice_y = -1
        else:
            self.roll_dice_y = 1
