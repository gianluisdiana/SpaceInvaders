import pygame, sys, random
from obstacle import Obstacle
from alien import Alien, ExtraAlien
from player import Player

class SpaceInvaders:
    """Class to represent a space invaders game.

    Attributes:
        screen (pygame.Surface):
            The screen on which the game will be displayed.
        clock (pygame.time.Clock):
            The clock that will be used to control the game's FPS.
        fps (int):
            How many FPS the game will run at.
        player (Player):
            The player of the game.
        obstacles (pygame.sprite.Group):
            A group of Obstacles (groups of Blocks) of the game.
        aliens (pygame.sprite.Group):
            The aliens of the game.
        alien_lasers (pygame.sprite.Group):
            The lasers shot by the aliens.
        extra_alien (pygame.sprite.GroupSingle):
            An extra bonus alien.
        background_music (pygame.mixer.Sound):
            The background music of the game.
        explosion_sound (pygame.mixer.Sound):
            The sound that will be played when an alien is destroyed.
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
        self.player = Player(size)

        # Obstacle setup
        self.obstacles = pygame.sprite.Group()
        self.create_multiple_obstacles(size[0] / 15, 480, 6)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.create_alien_grid((6, 8))
        self.alien_lasers = pygame.sprite.Group()

        # Extra alien
        self.extra_alien = pygame.sprite.GroupSingle()
        ExtraAlien.SPAWN_TIME = random.randint(40, 80)

        # Audio setup
        self.background_music = pygame.mixer.Sound('./audio/background.wav')
        self.background_music.set_volume(.1)
        self.background_music.play(loops=-1)
        self.explosion_sound = pygame.mixer.Sound('./audio/explosion.wav')
        self.explosion_sound.set_volume(.2)

    def remove_sprites(self) -> None:
        """Remove all the sprites from the game."""
        self.aliens.empty()
        self.alien_lasers.empty()
        self.obstacles.empty()
        self.extra_alien.empty()

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
            elif event.type == SpaceInvaders.ALIENLASER_EVENT:
                self.random_alien_shoots()
            elif event.type == pygame.KEYDOWN:
                self.player.get_input(event, SpaceInvaders.ALIENLASER_EVENT)

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
                    self.player.increase_score(alien.points)
                laser.kill()
                self.explosion_sound.play()
            if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                self.player.increase_score(500)
                laser.kill()
                self.explosion_sound.play()
            if pygame.sprite.spritecollide(laser, self.obstacles, True):
                self.player.reset_multiplier()
                laser.kill()

        # Alien lasers
        for laser in self.alien_lasers:
            if pygame.sprite.spritecollide(laser, self.player, False):
                self.player.lives.decrease()
                if self.player.is_dead():
                    self.player.save_score()
                    pygame.quit()
                    sys.exit()
                laser.kill()
            if pygame.sprite.spritecollide(laser, self.obstacles, True):
                laser.kill()

        # Aliens
        for alien in self.aliens:
            pygame.sprite.spritecollide(alien, self.obstacles, True)
            if pygame.sprite.spritecollide(alien, self.player, False):
                self.player.save_score()
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

    def update_sprites(self) -> None:
        """Update all the sprites."""
        self.player.update()
        self.aliens.update()
        self.extra_alien.update()
        self.alien_lasers.update()

    def victory_message(self) -> None:
        """Show a message when the player wins."""
        if not self.aliens.sprites():
            self.player.save_score()

            font = pygame.font.Font('./fonts/Pixeled.ttf', 20)
            victory_text = font.render('You Won!', True, (255, 255, 255))
            victory_rect = victory_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
            self.screen.blit(victory_text, victory_rect)

    def run(self) -> None:
        """Start the game loop."""
        while True:
            self.get_input()

            if not self.player.name_introduced:
                self.screen.fill((30, 30, 30))
                self.player.ask_name(self.screen)

            else:
                self.update_sprites()

                self.check_aliens_position()
                self.check_extra_alien_timer()
                self.check_collitions()

                self.draw()
                self.victory_message()

            pygame.display.flip()
            self.clock.tick(self.fps)