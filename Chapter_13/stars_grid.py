import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from stars import Stars
from random import randint
class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._create_fleet()
        #Set background color
        self.bg_color = (230, 230, 230)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Make an alien
        stars = Stars(self)
        alien_width, alien_height = stars.rect.size
        #get the width from the first alien width
        current_x, current_y = alien_width, alien_height
        #we keep adding aliens if there's enough room
        #to determine if we got enough room:
        #compare current_x to some maximum value
        #current_x < self.settings.screen_width might work but it will misplace the final alien
        #so we have to add a little margin (- 2 * alien_width)
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Stars(self)
        new_alien.rect.x = x_position + self._get_star_offset()
        new_alien.rect.y = y_position + self._get_star_offset()
        self.stars.add(new_alien)

    def _get_star_offset(self):
        """Return a random adjustment to a star's position"""
        offset_size = 15
        return randint(-1*offset_size, offset_size)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._update_screen()
            self.clock.tick(60) #frame rate of 60fps

    def _update_screen(self):
        """Update image on screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
