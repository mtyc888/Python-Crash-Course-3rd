import pygame
from settings import Settings
class Rocket:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        #Store a float for the ship's exact horizontal position
        self.y = float(self.rect.y)
        #movement flag; start with a ship that is not moving
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from position attributes.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)