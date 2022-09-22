import pygame, sys, random
from player import Player
from obstacle import Obstacle
from alien import Alien, ExtraAlien
from score import Score
from lives import Lives

class SpaceInvaders:
    """Class to represent a space invaders game.

    Attributes:
        screen (pygame.Surface):
            The screen on which the game will be displayed.
        clock (pygame.time.Clock):
            The clock that will be used to control the game's FPS.
        fps (int):
            How many FPS the game will run at.
        player (pygame.sprite.GroupSingle):
            The player of the game.
        obstacles (pygame.sprite.Group):
            A group of Obstacles (groups of Blocks) of the game.
        aliens (pygame.sprite.Group):
            The aliens of the game.
        alien_lasers (pygame.sprite.Group):
            The lasers shot by the aliens.
        extra_alien (pygame.sprite.GroupSingle):
            An extra bonus alien.
        score (Score):
            The score the player currently has.
        lives (Lives):
            The lives of the player.
    """

    OBSTACLE_AMOUNT = 4
    """The amount of obstacle the game will have."""

    ALIENLASER_EVENT = pygame.USEREVENT + 1
    """The event that will be triggered when an alien shoots a laser."""

    def create_multiple_obstacles(self, x_start: int, y_start: int, block_size: int) -> None:
        """Create multiple obstacles in the screen.

        Args:
            x_start (int): The x position where the first obstacle will be created.
            y_start (int): The y position where all the obstacles will be created.
            block_size (int): The size of the blocks that will compose the obstacles.
        """
        offsets = [num * (self.screen.get_width() / SpaceInvaders.OBSTACLE_AMOUNT) for num in range(self.OBSTACLE_AMOUNT)]
        for offset_x in offsets:
            self.obstacles.add(Obstacle(block_size, (241, 79, 80), (x_start + offset_x, y_start)))

    def create_alien_grid(self, size: tuple[int], x_distance: int = 60, y_distance: int = 48) -> None:
        """Create the grid of aliens.

        Args:
            size (tuple[int, int]): The size of the grid (num_rows, num_cols).
            x_distance (int, optional): The distance between each alien in the x axis. Defaults to 60.
            y_distance (int, optional): The distance between each alien in the y axis. Defaults to 48.
        """
        rows, cols = size
        for row_index in range(rows):
            for col_index in range(cols):
                x = 70 + col_index * x_distance
                y = 100 + row_index * y_distance

                if row_index == 0:
                    color = 'yellow'
                elif 1 <= row_index <= 2:
                    color = 'green'
                else:
                    color = 'red'
                self.aliens.add(Alien(color, (x, y)))

    def __init__(self, size: tuple[int], fps: int = 60):
        """Initialize all the requirements for the game.

        Args:
            size (tuple[int, int]): The size of the screen (width, height).
            fps (int, optional): The FPS of the game. Defaults to 60.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Player setup
        player_sprite = Player((size[0] / 2, size[1]), 5, size[0])
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle setup
        self.obstacles = pygame.sprite.Group()
        self.create_multiple_obstacles(size[0] / 15, 480, 6)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.create_alien_grid((6, 8))
        self.alien_lasers = pygame.sprite.Group()
        pygame.time.set_timer(SpaceInvaders.ALIENLASER_EVENT, 1000)

        # Extra alien
        self.extra_alien = pygame.sprite.GroupSingle()
        ExtraAlien.SPAWN_TIME = random.randint(40, 80)

        # Health and score setup
        self.score = Score((10, -10), (255, 255, 255))
        self.lives = Lives(3, size[0])

    def random_alien_shoots(self) -> None:
        """Choose a random alien to shoot a laser"""
        if not self.aliens.sprites(): return

        random_alien = random.choice(self.aliens.sprites())
        self.alien_lasers.add(random_alien.shoot(self.screen.get_height()))

    def get_input(self) -> None:
        """Get the input from the player."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SpaceInvaders.ALIENLASER_EVENT:
                self.random_alien_shoots()

    def move_aliens_down(self, distance: int) -> None:
        """Move all the aliens down a certain distance.

        Args:
            distance (int): The distance the aliens will move down.
        """
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.move_down(distance)

    def check_aliens_position(self) -> None:
        """Check if the aliens have reached the screen border."""
        all_aliens = self.aliens.sprites()
        if any(alien.found_border(self.screen.get_width()) for alien in all_aliens):
            Alien.change_direction()
            self.move_aliens_down(10)

    def spawn_extra_alien(self) -> None:
        """Spawn an extra alien in the screen."""
        side = random.choice(['left', 'right'])
        self.extra_alien.add(ExtraAlien(side, self.screen.get_width()))
        ExtraAlien.SPAWN_TIME = random.randint(400, 800)

    def check_extra_alien_timer(self) -> None:
        """Check if the extra alien should be spawned."""
        ExtraAlien.SPAWN_TIME -= 1
        if ExtraAlien.SPAWN_TIME <= 0:
            self.spawn_extra_alien()

    def check_collitions(self) -> None:
        """Check if there are any collitions between the sprites."""
        # Player lasers
        for laser in self.player.sprite.lasers:
            aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
            if aliens_hit:
                for alien in aliens_hit:
                    self.score.increase(alien.points)
                laser.kill()
            if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                self.score.increase(500)
                laser.kill()
            if pygame.sprite.spritecollide(laser, self.obstacles, True):
                laser.kill()

        # Alien lasers
        for laser in self.alien_lasers:
            if pygame.sprite.spritecollide(laser, self.player, False):
                self.lives.decrease()
                if self.lives.is_empty():
                    pygame.quit()
                    sys.exit()
                laser.kill()
            if pygame.sprite.spritecollide(laser, self.obstacles, True):
                laser.kill()

        # Aliens
        for alien in self.aliens:
            pygame.sprite.spritecollide(alien, self.obstacles, True)
            if pygame.sprite.spritecollide(alien, self.player, False):
                alien.kill()
                sys.exit()

    def draw(self) -> None:
        """Draw all the images in the screen."""
        self.screen.fill((30, 30, 30))
        self.player.draw(self.screen)
        self.aliens.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.extra_alien.draw(self.screen)
        self.player.sprite.lasers.draw(self.screen)
        self.alien_lasers.draw(self.screen)
        self.score.draw(self.screen)
        self.lives.draw(self.screen)

    def update_sprites(self) -> None:
        """Update all the sprites."""
        self.player.update()
        self.aliens.update()
        self.extra_alien.update()
        self.alien_lasers.update()

    def run(self) -> None:
        """Start the game loop."""
        while True:
            self.get_input()

            self.update_sprites()

            self.check_aliens_position()
            self.check_extra_alien_timer()
            self.check_collitions()

            self.draw()

            pygame.display.flip()
            self.clock.tick(self.fps)