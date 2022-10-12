import sys
from os import path
from space_invaders import SpaceInvaders

def check_custom(argv: tuple[str]) -> str:
    """Checks if the user wants to use a custom configuration.

    Args:
        argv (tuple[str]): The command line arguments.

    Returns:
        str: The custom configuration folder's name formated.
    """
    if not path.exists('./custom'):
        raise FileNotFoundError('The folder for the custom configurations does not exist.')

    if (len(argv) != 3 or argv[1] != "--custom"):
        return './'

    if not path.exists(f'./custom/{argv[2]}'):
        raise FileNotFoundError(f'The custom folder "{argv[2]}" does not exist.')

    return f'./custom/{argv[2]}/'

def main():
    custom_path = check_custom(sys.argv)
    game = SpaceInvaders((600, 600), custom_path=custom_path)
    game.run()

if __name__ == '__main__':
    main()