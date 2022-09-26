import pygame, json
from spaceship import Spaceship
from score import Score
from lives import Lives

class Player(pygame.sprite.GroupSingle):
    """Represents the player of the game.

    Attributes:
        name (str):
            The name of the player.
        score (Score):
            The score the player currently has.
        lives (Lives):
            The lives of the player.
        name_introduced (bool):
            If the player has already introduced his name.
        text_font (pygame.font.Font):
            The font of the text used to ask the name and display it.
    """

    def __init__(self, screen_size: tuple[int, int]):
        """Initialize the player.

        Args:
            screen_size (tuple[int, int]): The size of the screen (width, height).
        """
        width, height = screen_size
        self.name = ''
        self.name_introduced = False
        self.score = Score((10, -10), (255, 255, 255))
        self.lives = Lives(3, width)
        self.text_font = pygame.font.Font('./fonts/Pixeled.ttf', 20)
        super().__init__(Spaceship((width / 2, height), 5, width))

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player on the screen.

        Args:
            screen (pygame.Surface): The screen where the player will be drawn.
        """
        super().draw(screen)
        self.score.draw(screen)
        self.lives.draw(screen)

    def is_dead(self) -> bool:
        """Check if the player is dead.

        Returns:
            bool: True if the player is dead, False otherwise.
        """
        return self.lives.is_empty()

    def increase_score(self, points: int) -> None:
        """Increase the score of the player.

        Args:
            points (int): The points to increase the score.
        """
        self.score.increase(points)
        self.score.increase_multiplier()

    def save_score(self) -> None:
        """Save the score of the player."""
        with open('scores.json', 'r+') as file:
            json_file = file.read()
            dct_score = json.loads(json_file)
            dct_score[self.name] = self.score.value

            file.seek(0)
            file.write(json.dumps(dct_score, indent=2))
            file.truncate()

    def display_name(self, screen: pygame.Surface) -> None:
        """Display the name of the player.

        Args:
            screen (pygame.Surface): The screen where the name will be displayed.
        """
        name_text = self.text_font.render(self.name, True, (255, 255, 255))
        name_rect = name_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(name_text, name_rect)

    def ask_name(self, screen: pygame.Surface) -> None:
        """Ask the name of the player.

        Args:
            screen (pygame.Surface): The screen where the name will be asked.
        """
        petition_text = self.text_font.render("Introduce your name:", True, (255, 255, 255))
        petition_rect = petition_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(petition_text, petition_rect)
        self.display_name(screen)

    @staticmethod
    def name_already_registered(name: str) -> bool:
        """Check if the name of the player is registered.

        Args:
            name (str): The name of the player.

        Returns:
            bool: True if the name is registered, False otherwise.
        """
        with open('scores.json', 'r') as file:
            json_file = file.read()
            dct_score = json.loads(json_file)
            return name in dct_score

    def get_input(self, event: pygame.event.Event, alien_event: int) -> None:
        """Get the input of the player.

        Args:
            event (pygame.event.Event): The event produced.
            alien_event (int): The event that will be triggered when an alien shoots a laser
        """
        if not self.name_introduced:
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.key == pygame.K_RETURN:
                if not Player.name_already_registered(self.name):
                    self.name_introduced = True
                    pygame.time.set_timer(alien_event, 1000)
            else:
                self.name += event.unicode

    def reset_multiplier(self) -> None:
        """Reset the score's multiplier."""
        self.score.reset_multiplier()

    def update(self) -> None:
        """Update the player's ship and lasers."""
        for laser in self.sprite.lasers:
            if laser.is_off_screen():
                self.score.reset_multiplier()
        super().update()