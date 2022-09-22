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
    """

    def __init__(self, pos: tuple[int], speed: int):
        """Initialize the laser with the image to display, position and speed.

        Args:
            pos (tuple[int, int]): The x and y position of the laser.
            speed (int): The speed (in pixels) the laser will travel.
        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed