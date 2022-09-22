import pygame

class Block(pygame.sprite.Sprite):
    """Represent an obstacle block.

    Attributes:
        image (pygame.Surface): The block's image that will be displayed.
        rect (pygame.Rect): The measured surface of the block.
    """

    def __init__(self, side_length: int, color: tuple[int], pos: tuple[int]):
        """Initialize the block with the image to display and its position.

        Args:
            side_length (int): The length of the block's side.
            color (tuple[int, int, int]): The RGB color of the block.
            pos (tuple[int, int]): The position of the block (x, y).
        """
        super().__init__()
        self.image = pygame.Surface((side_length, side_length))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class Obstacle(pygame.sprite.Group):
    """Represents an obstacle.

    Attributes:
        block_size (int): The length of the block's side.
        color (tuple[int, int, int]): The RGB color of the block.
        pos (tuple[int, int]): The position of the block (x, y).
    """

    def __init__(self, block_size: int, color: tuple[int], pos: tuple[int]):
        """Initialize the obstacle with the blocks to display and its position.

        Args:
            side_length (int): The length of the block's side.
            color (tuple[int, int, int]): The RGB color of the block.
            pos (tuple[int, int]): The position of the block (x, y).
        """
        super().__init__()
        self.block_size = block_size
        self.color = color
        self.pos = pos