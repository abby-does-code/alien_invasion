##START##
# First Development Phase#

# install pygame using "pip3 install pygame"
##install successful

# Starting Game Project
##Begin by creating empty Pygame window and responding to user output

import sys
import pygame
from settings import Settings

# Importing settings into the main file and adjust parameters to teh SEttings listed.
from ship import Ship

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
        # Set a background color:
        self.ship = Ship(self)
        self.bg_color = (230, 230, 230)  # Specified as RGB colors

    def run_game(self):  # Game is controlled by the run game method.
        """Start the main loop for game."""
        while True:  # Manages screen updates
            self._check_events()
            self._update_screen()

            def _check_events(self):
                """Respond to keypresses and mouse events."""
                for event in pygame.even.get():
                    if event.type == pygame.QUIT:
                        sys.exit
                # Watch for keyboard/mouse events
                # Event loop listens for events (action user performs) and performs apprpriate tasks depending on the event:

            def _update_screen(self):
                # Redraw the screen
                self.screen.fill(self.settings.bg_color)  # fills with selected color
                # Make most recently drawn screen visible; continually updates display:
                self.ship.blitme()

            pygame.display.flip()

        # Make a game instance, then run. Only runs if file is called directly:
        if __name__ == "main":
            ai = AlienInvasion()
            ai.run.game()
