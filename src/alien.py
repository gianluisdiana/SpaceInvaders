from pygame import image
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents an alien.

    Attributes:
        image (pygame.Surface): The alien's image that will be displayed.
        rect (pygame.Rect): The measured rectangle of the alien.
    """

    def __init__(self, color: str, pos: tuple[int]):
        """Initialize the alien with the image to display, position and points.

        Args:
            color (str): The color of the alien.
            pos (tuple[int, int]): The position of the alien (x, y).
        """
        super().__init__()
        self.image = image.load(f'../graphics/aliens/{color}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)