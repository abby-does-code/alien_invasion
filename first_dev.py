##START##
# First Development Phase#

# install pygame using "pip3 install pygame"
##install successful

# Starting Game Project
##Begin by creating empty Pygame window and responding to user output

import sys
import pygame
from settings import Settings
from ship import Ship as Ship

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
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set a background color:
        self.bg_color = (230, 230, 230)  # Specified as RGB colors

    def run_game(self):  # Game is controlled by the run game method.

        """Start the main loop for game."""

        while True:
            self.ship.update()
            self._check_events()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                # Watch for keyboard/mouse events
                # Event loop listens for events (action user performs) and performs apprpriate tasks depending on the event
                # If KEYDOWN happens, moving_direction funciton is set to True; otherwise, set back to False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make most recently drawn screen visible:

        pygame.display.flip()

        # Make a game instance, then run. Only runs if file is called directly:


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
