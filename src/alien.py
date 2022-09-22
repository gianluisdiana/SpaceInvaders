from pygame import image
from pygame.sprite import Sprite
from laser import Laser

class Alien(Sprite):
    """Represents an alien.

    Attributes:
        image (pygame.Surface): The alien's image that will be displayed.
        rect (pygame.Rect): The measured rectangle of the alien.
        points (int): The points the player will get if the alien is destroyed.
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

        if color == 'red':
            self.points = 100
        elif color == 'green':
            self.points = 200
        else:
            self.points = 300

    def update(self) -> None:
        """Move the alien horizontally."""
        self.rect.x += Alien.X_DIRECTION

    @staticmethod
    def change_direction() -> None:
        """Change the direction the alien will move."""
        Alien.X_DIRECTION *= -1

    def move_down(self, distance: int) -> None:
        """Move the alien down.

        Args:
            distance (int): The distance the alien will move down.
        """
        self.rect.y += distance

    def found_border(self, screen_width: int) -> bool:
        """Check if the alien found a border.

        Args:
            screen_width (int): The width of the game screen.

        Returns:
            True if the alien found a border, False otherwise.
        """
        return self.rect.right >= screen_width or self.rect.left <= 0

    def shoot(self, y_limit: int) -> Laser:
        """Create a new laser and return it.

        Args:
            y_limit (int): The y limit the laser may travel.

        Returns:
            The laser shot by the alien.
        """
        laser = Laser(self.rect.center, 6, y_limit)
        return laser

class ExtraAlien(Alien):
    """Represents the bonus extra alien.

    Attributes:
        image (pygame.Surface): The alien's image that will be displayed.
        rect (pygame.Rect): The measured rectangle of the alien.
        speed (int): The speed (in pixels) the alien will travel.
        points (int): The points the player will get if the alien is destroyed.
    """

    SPAWN_TIME = 1
    """The spawn time left for the alien to appear."""

    def __init__(self, side: str, screen_width: int):
        """Initialize the alien with the image to display, position and points.

        Args:
            side (str): The side of the screen where the alien will appear.
            screen_width (int): The width of the game screen.
        """
        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
        super().__init__('extra', (x, 70))
        self.points = 500

    def update(self) -> None:
        """Move the alien horizontally."""
        self.rect.x += self.speed