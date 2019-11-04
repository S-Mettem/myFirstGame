"""
    :param PING PONG GAME BY ILYA GADALOV
    module pygame
    main program file
"""
# import file
import pygame
import game_function as gf
from settings import Settings
from player import Player
from ball import Ball
from Scoreboard import Scoreboard
from Button import Button


def run_game():
    # initialization pygame module
    pygame.init()

    # initialization all objects and screen
    # Settings
    settings = Settings(1200, 800, "Pong Game")

    # screen
    # set Width and height
    screen = pygame.display.set_mode((settings.screen_height,
                                      settings.screen_width))
    screen_rect = screen.get_rect()
    # set name of Window
    pygame.display.set_caption(settings.window_name)

    # Player class
    player_1 = Player(settings, screen, (255, 0, 0),
                      screen_rect.left + 3 * settings.player_width)
    player_2 = Player(settings, screen, (0, 0, 255),
                      (screen_rect.left + screen_rect.right - 3 *
                       settings.player_width))

    # Ball class
    ball = Ball(settings, screen)

    # Scoreboard for two players
    # For 1st player
    score_for_player_1 = Scoreboard(screen, player_1,
                                    screen_rect.left + player_1.rect.height,
                                    screen_rect.top + player_1.rect.height)
    # For 2st player
    score_for_player_2 = Scoreboard(screen, player_2,
                                    screen_rect.right - player_2.rect.height,
                                    screen_rect.top + player_2.rect.height)

    # Class Buttons
    start_button = Button(screen, 100, 100, screen_rect.centerx,
                          screen_rect.centery, 'Play', 48,
                          (107, 209, 52), bold=True)
    while True:
        """main cycle to update screen and key events"""
        if settings.game_active:
            """Functions to game active settings"""
            player_1.update()
            player_2.update()
            ball.update()
            gf.goal(screen, score_for_player_1, score_for_player_2,
                    ball, player_1, player_2)
            gf.check_border_screen(screen, ball, player_1, player_2)

        gf.check_key_event(settings, player_1, player_2, start_button)
        gf.update_screen(settings, screen, score_for_player_1,
                         score_for_player_2, player_1, player_2, ball,
                         start_button)


# main function to start main function
if __name__ == '__main__':
    run_game()
