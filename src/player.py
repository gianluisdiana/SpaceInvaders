from pygame.sprite import GroupSingle

class Player(GroupSingle):
    """Represents the player of the game.

    Attributes:
        name (str):
            The name of the player.
        ship (Spaceship):
            The sprite of its spaceship.
        score (Score):
            The score the player currently has.
        lives (Lives):
            The lives of the player.
    """