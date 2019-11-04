"""

    Class Player is platform to racket

"""
import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, settings, screen, color, position_x):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create rectangle rocket
        self.rect = pygame.Rect(0, 0, settings.player_width,
                                settings.player_height)

        # Position rocket
        self.rect.left = position_x
        self.rect.centery = self.screen_rect.centery

        # Other settings
        self.color = color
        self.speed = settings.player_speed
        self.move_up = False
        self.move_down = False
        self.score = 0

    def update(self):
        if self.move_up:
            if self.rect.top != self.screen_rect.top:
                self.rect.y -= self.speed
        if self.move_down:
            if self.rect.bottom != self.screen_rect.bottom:
                self.rect.y += self.speed

    def self_draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
