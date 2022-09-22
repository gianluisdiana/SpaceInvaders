import pygame

class Player(pygame.sprite.Sprite):
    """Represents the player's spaceship.

    Attributes:
        image (pygame.Surface):
            The player's image that will be displayed.
        rect (pygame.Rect):
            The measured rectangle of the player.
        speed (int):
            The speed (in pixels) the player will travel.
    """

    def __init__(self, pos: tuple[int], speed: int):
        """Initialize the player with the image to display.

        Args:
            pos (tuple[int, int]): The position of the player (x, y).
            speed (int): The speed (in pixels) the player will travel.
        """
        super().__init__()
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed

    def get_input(self) -> None:
        """Get the player's input and move the player."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed