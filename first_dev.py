##START##

# install pygame using "pip3 install pygame"
##install successful


import sys
from time import sleep  # so we can pause the game

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button

from ship import Ship as Ship
from bullet import Bullet

from alien import Alien


# Importing sys and pygame modules; pygame for functionality and sys tools to quit.


class AlienInvasion:  # Starting point!
    """Overall class to manage game assets and behaviors."""

    def __init__(self):  # Initializes background settings.
        """Initialize the game, and create game resources."""

        pygame.init()

        self.settings = Settings()

        # Creates display window; available to all methods in class:
        ## Surface: part of screen where game happens):
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Set a background color:
        self.bg_color = (230, 230, 230)  # Specified as RGB colors
        pygame.display.set_caption("Alien Invasion")

        """ Code for full screen:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        """

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):  # Game is controlled by the run game method.
        """Start the main loop for game."""
        while True:
            self._check_events()
            # self._update_screen()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    ##############################################################
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  # separating out blocks of code
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
            ):  # python detects whenever player clicks
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    ##############################################################
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics
            self.stats.reset_stats()
            # check to make sure button is hit
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    ##############################################################
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  # Allows player to quit with q
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    ##############################################################
    def _check_keyup_events(self, event):
        """Respond to keyup events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

            # Watch for keyboard/mouse events
            # Event loop listens for events (action user performs) and performs apprpriate tasks depending on the event
            # If KEYDOWN happens, moving_direction funciton is set to True; otherwise, set back to False

    ##############################################################
    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    ##############################################################
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # update bullet positions
        self.bullets.update()  # calls for update on every sprit ein group

        # Get rid of old bullets
        for bullet in self.bullets.copy():  # loop allow sus to modify
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    ##############################################################
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine teh number of rows of aliens that fit on teh scree
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    ##############################################################
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    ##############################################################
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship got hit
                self._ship_hit()
                break

    ##############################################################
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in
        the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom
        self._check_aliens_bottom()

    ##############################################################
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    ##############################################################
    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the play button if teh game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make most recently drawn screen visible:
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

# Make a game instance, then run. Only runs if file is called directly:
