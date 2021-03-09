import pygame
from pygame.sprite import Sprite

# When you use sprites, you can group related elements in the game and act on
# all the grouped elements at once


class Bullet(Sprite):
    """A class to maange bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        # Bullet isn't image based so we build from scratch
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        # sets the bullet's midtop attribute equal to the ship's midtop attribute

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    # Update method manages the bullet's position
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of bullet
        self.y -= self.settings.bullet_speed
        # decreasing y value; allows us to increase bullet speed

        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)