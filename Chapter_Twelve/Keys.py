import sys
import pygame
from rocket import Rocket
from settings import Settings
class Keys:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.rocket = Rocket(self)
        #Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60) #frame rate of 60fps

    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self,event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update image on screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game
    ai = Keys()
    ai.run_game()
