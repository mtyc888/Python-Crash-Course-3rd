import pygame

class Bird:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/bird_small.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)