"""
    CLASS BALL
        is not control

"""
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, settings, screen):
        super(Sprite).__init__()
        # Create screen
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Create and place a ball at screen
        self.rect = pygame.Rect(0, 0, settings.ball_radius, settings.ball_radius)
        self.rect.center = self.screen_rect.center

        # Other attributes
        self.color = (255, 255, 255)
        self.speed = settings.ball_speed
        self.directionX = settings.roll_dice_x
        self.directionY = settings.roll_dice_y

    def update(self):
        self.rect.x += self.speed * self.directionX
        self.rect.y += self.speed * self.directionY

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
