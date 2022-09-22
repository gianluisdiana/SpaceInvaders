import pygame

class Laser(pygame.sprite.Sprite):
    """Represents a laser object that can be fired by the player or the aliens.

    Attributes:
        image (pygame.Surface):
            The laser's image that will be displayed.
        rect (pygame.Rect):
            The measured rectangle of the laser.
        speed (int):
            The speed (in pixels) the laser will travel.
        y_limit (int):
            The maximum y position the laser can reach.
    """

    def __init__(self, pos: tuple[int], speed: int, screen_height: int):
        """Initialize the laser with the image to display, position and speed.

        Args:
            pos (tuple[int, int]): The x and y position of the laser.
            speed (int): The speed (in pixels) the laser will travel.
            screen_height (int): The height of the game screen.
        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.y_limit = screen_height

    def is_off_screen(self) -> bool:
        """Check if the laser is off the screen.

        Returns:
            bool: True if the laser is off the screen, False otherwise.
        """
        return self.rect.bottom <= 0 or self.rect.top >= self.y_limit

    def update(self) -> None:
        """Update the laser's position."""
        self.rect.y += self.speed
        if self.is_off_screen(): self.kill()