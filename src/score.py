from pygame import Surface
from pygame.font import Font

class Score:
    """Score class for the game.

    Attributes:
        pos (tuple[int, int]): The x and y position of the score.
        color (tuple[int, int, int]): The RGB color code.
        value (int): The current score.
        font (pygame.font.Font): The font of the message displayed.
    """

    def __init__(self, pos: tuple[int], color: tuple[int]) -> None:
        """Initialize the score class.

        Args:
            pos (tuple[int, int]): The x and y position of the score.
            color (tuple[int, int, int]): The RGB color code.
        """
        self.pos = pos
        self.color = color
        self.value = 0
        self.font = Font('../fonts/Pixeled.ttf', 20)

    def increase(self, value: int = 1) -> None:
        """Increase the score.

        Args:
            value: An integer indicating the value to increase the score.
        """
        self.value += value

    def reset(self) -> None:
        """Reset the score."""
        self.value = 0

    def draw(self, screen: Surface) -> None:
        """Draw the score on the screen."""
        score = self.font.render(f"Score: {self.value}", True, self.color)
        screen.blit(score, self.pos)