import pygame
from laser import Laser

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
        ready_to_shoot (bool):
            If the player is ready to shoot.
        laser_cooldown (int):
            The time (in milliseconds) the player needs to wait to recharge the laser.
        laser_time (int):
            The time (in milliseconds) the player last shot a laser.
        lasers (pygame.sprite.Group):
            The lasers shot by the player.
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

        self.ready_to_shoot = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.lasers = pygame.sprite.Group()

    def shoot_laser(self) -> None:
        """Create a new laser and add it to the lasers group."""
        laser = Laser(self.rect.center, -8)
        self.lasers.add(laser)
        self.laser_time = pygame.time.get_ticks()
        self.ready_to_shoot = False

    def get_input(self) -> None:
        """Get the player's input and move the player."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready_to_shoot:
            self.shoot_laser()

    def check_border(self) -> None:
        """Keep the player on the screen if it founds a wall."""
        if self.rect.right >= self.x_limit:
            self.rect.right = self.x_limit
        elif self.rect.left < 0:
            self.rect.left = 0

    def recharge(self) -> None:
        """Recharge the player's laser."""
        if not self.ready_to_shoot:
            now = pygame.time.get_ticks()
            if now - self.laser_time >= self.laser_cooldown:
                self.ready_to_shoot = True

    def update(self) -> None:
        """Update the player's position and recharge the laser."""
        self.get_input()
        self.check_border()
        self.recharge()