# Tracks Game statistics


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactivate state
        self.game_active = False

        # High score should never be reset(put in __init__ instead of reset)
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0