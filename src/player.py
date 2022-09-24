from pygame.sprite import GroupSingle
from spaceship import Spaceship
from score import Score
from lives import Lives

class Player(GroupSingle):
    """Represents the player of the game.

    Attributes:
        name (str):
            The name of the player.
        score (Score):
            The score the player currently has.
        lives (Lives):
            The lives of the player.
    """

    def __init__(self, name: str, screen_size: tuple[int, int]):
        """Initialize the player.

        Args:
            name (str): The name of the player.
            screen_size (tuple[int, int]): The size of the screen (width, height).
        """
        width, height = screen_size
        self.name = name
        self.score = Score((10, -10), (255, 255, 255))
        self.lives = Lives(3, width)
        super().__init__(Spaceship((width / 2, height), 5, width))