import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self._create_fleet()
        #Set background color
        self.bg_color = (230, 230, 230)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
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
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.alien.add(new_alien)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60) #frame rate of 60fps

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.alien.update()

    def _update_bullets(self):
        self.bullets.update()
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        
    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            #Fire a bullet
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update image on screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #draw the ship onto the screen
        self.ship.blitme()
        self.alien.draw(self.screen)
        #Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_fleet_edges(self):
        """Response appropriately when the fleet reaches the edge"""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # 1* - 1 = -1
        # -1 * -1 = 1
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
