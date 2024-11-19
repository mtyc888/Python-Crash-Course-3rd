import pygame
from pygame.sprite import Sprite

class Stars(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        """Initialize he alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set it's rect
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

