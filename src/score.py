from pygame import Surface
from pygame.font import Font

class Score:
    """Score class for the game.

    Attributes:
        pos (tuple[int, int]):
            The x and y position of the score.
        color (tuple[int, int, int]):
            The RGB color code.
        value (int):
            The current score.
        font (pygame.font.Font):
            The font of the message displayed.
        multiplier (float):
            A certain amount to multiply the score when is increased.
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
        self.multiplier = 1
        self.font = Font('./fonts/Pixeled.ttf', 20)

    def increase(self, value: int = 1) -> None:
        """Increase the score.

        Args:
            value (int, optional): Indicates the value to increase the score. 1 by default.
        """
        self.value += value * self.multiplier

    def reset(self) -> None:
        """Reset the score."""
        self.value = 0
        self.multiplier = 1

    def draw(self, screen: Surface) -> None:
        """Draw the score on the screen.

        Args:
            screen (pygame.Surface): The screen where the score will be drawn.
        """
        score_text = self.font.render(f"Score: {self.value:.2f}", True, self.color)
        screen.blit(score_text, self.pos)
        if self.multiplier != 1:
            multiplier_text = self.font.render(f"Multiplier: {self.multiplier:.2f}", True, self.color)
            screen.blit(multiplier_text, (self.pos[0], self.pos[1] + 30))

    def increase_multiplier(self, amount: int = .05) -> None:
        """Increase the multiplier.

        Args:
            amount (int, optional): The amount to increase the multiplier. 0.5 by default.
        """
        self.multiplier += amount

    def reset_multiplier(self) -> None:
        """Reset the multiplier to 1."""
        self.multiplier = 1