import sys
import pygame
from ship import Ship
from bird import Bird
class BlueBird:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bird = Bird(self)
        #Set background color
        self.bg_color = (0, 0, 0)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60) #frame rate of 60fps

    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Update image on screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        #draw the ship onto the screen
        self.bird.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game
    ai = BlueBird()
    ai.run_game()
