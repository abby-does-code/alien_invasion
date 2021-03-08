import pygame

# Creating ship module that will contain the ship class and manage its behavior


class Ship:
    """A class to mange the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_Rect = ai_game.screen.get_rect()
        # Allows us to place the ship in the appropriate

        # Load ship image and get its rect:
        self.image = pygame.image.load("images/ship.bmp")  # calling the image
        self.rect = self.image.get_rect()  # access the ship's rect attribute

        # Start each new ship at the bottom of the screen:
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(Self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        def update(self):
            """Update the ship's position based on the movemnet flag."""
            # Update ship's x value, not the rect

            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed  # Moves if true

            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed

            # Update rect object from self.x
            self.rect.x = self.x

    def blitme(self):
        # Draws the image to the screen at the position specified by self.rect
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)
