import pygame

class Lives:
    """Represents the remaining lives of the player.

    Attributes:
        amount (int):
            The number of lives the player has.
        inital_amount (int):
            The initial amount of lives the player has.
        image (pygame.Surface):
            The image that will be displayed.
        pos (tuple[int]):
            The position of the images.
    """

    def __init__(self, amount: int, screen_width: int):
        """Initialize the amount with the images to display and position.

        Args:
            amount (int): The number of lives the player has.
            screen_width (int): The width of the game screen.
        """
        self.initial_amount = self.amount = amount
        self.image = pygame.image.load('./images/player.png').convert_alpha()
        x = screen_width - self.image.get_width() - 10
        self.pos = (x, 10)

    def decrease(self) -> None:
        """Decrease the number of lives by one."""
        self.amount -= 1

    def is_empty(self) -> bool:
        """Return True if the player has no lives left."""
        return self.amount <= 0

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the lives on the screen.

        Args:
            screen (pygame.Surface): The game screen.
        """
        for live in range(self.amount - 1):
            x = self.pos[0] - live * (self.image.get_width() + 10)
            screen.blit(self.image, (x, self.pos[1]))

    def reset(self) -> None:
        """Reset the number of lives to the initial value."""
        self.amount = self.initial_amount