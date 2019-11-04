"""
    MAIN GAME FUNCTION


"""
# Imports modules
import sys
import pygame
from time import sleep
from Button import Button


# //////////////////////////////////////////////////////////
# //// Main function to update screen and event detects ////
def check_key_event(settings, player_1, player_2, start_button):
    """Detect pressed key"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            """Detect, when key button is down"""
            if event.key == pygame.K_w:
                player_1.move_up = True
            if event.key == pygame.K_s:
                player_1.move_down = True
            if event.key == pygame.K_UP:
                player_2.move_up = True
            if event.key == pygame.K_DOWN:
                player_2.move_down = True
            if event.key == pygame.K_SPACE and not settings.game_active:
                start_game(settings)
            if event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.KEYUP:
            """Detect, when key button is up"""
            if event.key == pygame.K_w:
                player_1.move_up = False
            if event.key == pygame.K_s:
                player_1.move_down = False
            if event.key == pygame.K_UP:
                player_2.move_up = False
            if event.key == pygame.K_DOWN:
                player_2.move_down = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            """Detect mouse event"""
            # Get position of mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check event to click at button's "Start" place
            button_start_clicked = start_button.rect.collidepoint(mouse_x,
                                                                  mouse_y)
            # If "Yes" than start a game
            if button_start_clicked and not settings.game_active:
                start_game(settings)


def start_game(settings):
    """Function to start a game"""
    # Hide cursor
    pygame.mouse.set_visible(False)
    # change flag game active
    settings.game_active = True
    # delay
    sleep(3)


def update_screen(settings, screen, score_for_player_1, score_for_player_2,
                  player_1, player_2, ball, start_button):
    # Background color
    screen.fill((158, 152, 152))
    # Draw 1st player
    player_1.self_draw()
    # Draw 2nd player
    player_2.self_draw()
    # Draw ball
    ball.draw_ball()
    # Show scoreboard 1st player
    score_for_player_1.show_score()
    # Show scoreboard 2nd player
    score_for_player_2.show_score()

    # Show button "Play", when game is not active
    if not settings.game_active:
        start_button.draw_button()

    # Print last screen
    pygame.display.flip()


# //////////////////////////////////////////////////////////////////////
# /////////////////////// Ball Control Function ///////////////////////
def check_border_screen(screen, ball, player_1, player_2):
    """Change direction of ball if detect collision with border of
       screen and players rackets"""
    # check collision between 1st player and ball at left and right side
    collision_with_p1 = pygame.sprite.collide_rect(player_1, ball)
    # check collision between 2st player and ball at left and right side
    collision_with_p2 = pygame.sprite.collide_rect(player_2, ball)

    screen_rect = screen.get_rect()
    # Bottom ball and screen border bottom
    if ball.rect.bottom == screen_rect.bottom:
        ball.directionY *= -1
    # Top ball and screen border top
    elif ball.rect.top == screen_rect.top:
        ball.directionY *= -1
    # Sprite ball and sprite player 1
    elif collision_with_p1:
        ball.directionX *= -1
    # Sprite ball and sprite player 2
    elif collision_with_p2:
        ball.directionX *= -1
    # Bottom ball and top player 1
    elif (ball.rect.bottom == player_1.rect.top and
          ball.rect.x == player_1.rect.x):
        ball.directionX *= -1
    # Top ball and bottom player 1
    elif (ball.rect.top == player_1.rect.bottom and
          ball.rect.x == player_1.rect.x):
        ball.directionX *= -1
    # Top ball and bottom player 2
    elif (ball.rect.top == player_2.rect.bottom and
          ball.rect.x == player_2.rect.x):
        ball.directionX *= -1
    # Bottom ball and top player 1
    elif (ball.rect.bottom == player_2.rect.top and
          ball.rect.x == player_2.rect.x):
        ball.directionX *= -1


# ///////////////////////////////////////////////////////
# ////////////////// Win settings //////////////////////
def goal(screen, score_for_player_1, score_for_player_2,
         ball, player_1, player_2):
    """Count score all players and reset game"""
    # Get screen rectangle
    screen_rect = screen.get_rect()
    if ball.rect.left == screen_rect.left:
        # Check to ball get to left side of screen
        # Then 1st player get one point to scoreboard
        player_2.score += 1
        # Reset game
        reset_after_goal(screen, score_for_player_1, score_for_player_2,
                         player_1, player_2, ball)

    elif ball.rect.right == screen_rect.right:
        # Check to ball get to right side of screen
        # Then 1st player get one point to scoreboard
        player_1.score += 1
        # Reset game
        reset_after_goal(screen, score_for_player_1, score_for_player_2,
                         player_1, player_2, ball)


def reset_after_goal(screen, score_for_player_1, score_for_player_2,
                     player_1, player_2, ball):
    """Reset game, place object to first position"""
    # place player 1
    player_1.rect.centery = screen.get_rect().centery
    score_for_player_1.prep_img()
    # place player 2
    player_2.rect.centery = screen.get_rect().centery
    score_for_player_2.prep_img()
    # place ball
    ball.rect.center = screen.get_rect().center
    # delay 3 second
    sleep(3)
