import pygame

class SpaceInvaders:
    """Class to represent a space invaders game.

    Attributes:
        screen (pygame.Surface):
            The screen on which the game will be displayed.
    """

    def __init__(self, size: tuple[int]):
        """Initialize all the requirements for the game.

        Args:
            size (tuple[int, int]): The size of the screen (width, height).
        """
        pygame.init()
        self.screen = pygame.display.set_mode(size)

    def run(self) -> None:
        """Start the game loop."""