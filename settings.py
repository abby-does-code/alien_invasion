##START##
##Creating a Settings Class##

###Allows us to work with jsut one settings object any time we need access to an individual setting. Easier to manage as game grows!###


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5  # adjusts 1.5 pixels at a time instead of 1
