from pygame import image
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents an alien.

    Attributes:
        image (pygame.Surface): The alien's image that will be displayed.
        rect (pygame.Rect): The measured rectangle of the alien.
    """

    X_DIRECTION = 1
    """The direction in the x axis the alien will move."""

    def __init__(self, color: str, pos: tuple[int]):
        """Initialize the alien with the image to display, position and points.

        Args:
            color (str): The color of the alien.
            pos (tuple[int, int]): The position of the alien (x, y).
        """
        super().__init__()
        self.image = image.load(f'../images/aliens/{color}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self) -> None:
        """Move the alien horizontally."""
        self.rect.x += Alien.X_DIRECTION