import pygame
from random import randint

class CRT:
    """Represents a CRT monitor filter.

    Attributes:
        tv_image (pygame.Surface): The edges of a crt monitor.
    """

    def __init__(self, size: tuple[int]) -> None:
        """Initializes the CRT class with its scaled image.

        Args:
            size (tuple[int]): The size of the screen.
        """
        self.tv_image = pygame.image.load('./images/tv.png').convert_alpha()
        self.tv_image = pygame.transform.scale(self.tv_image, size)

    def create_crt_lines(self) -> None:
        """Creates the lines on the screen."""
        distance_between_lines = 3
        line_amount = self.tv_image.get_height() // distance_between_lines
        for line in range(line_amount):
            y_pos = line * distance_between_lines
            pygame.draw.line(self.tv_image, 'black', (0, y_pos), (self.tv_image.get_width(), y_pos), 1)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the CRT filter on the screen.

        Args:
            screen (pygame.Surface): The screen to draw on.
        """
        self.tv_image.set_alpha(randint(40, 75))
        self.create_crt_lines()
        screen.blit(self.tv_image, (0, 0))