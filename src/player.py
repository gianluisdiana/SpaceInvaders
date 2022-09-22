import pygame

class Player(pygame.sprite.Sprite):
    """Represents the player's spaceship.

    Attributes:
        image (pygame.Surface):
            The player's image that will be displayed.
        rect (pygame.Rect):
            The measured rectangle of the player.
    """

    def __init__(self, pos: tuple[int]):
        """Initialize the player with the image to display.

        Args:
            pos (tuple[int, int]): The position of the player (x, y).
        """
        super().__init__()
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)