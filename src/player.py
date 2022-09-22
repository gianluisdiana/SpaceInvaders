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
        x_limit (int):
            The maximum x position the player can reach.
    """

    def __init__(self, pos: tuple[int], speed: int, screen_width: int):
        """Initialize the player with the image to display, position, speed and the screen x-limit.

        Args:
            pos (tuple[int, int]): The position of the player (x, y).
            speed (int): The speed (in pixels) the player will travel.
            screen_width (int): The width of the game screen.
        """
        super().__init__()
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.x_limit = screen_width

    def get_input(self) -> None:
        """Get the player's input and move the player."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def update(self) -> None:
        """Update the player's position."""
        self.get_input()