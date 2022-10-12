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

    if (len(argv) < 3 or "--custom" not in argv):
        return './'

    index_custom_folder = argv.index("--custom") + 1
    if (index_custom_folder >= len(argv)):
        raise ValueError('The custom folder name is missing.')

    folder_name = argv[index_custom_folder]

    if not path.exists(f'./custom/{folder_name}'):
        raise FileNotFoundError(f'The custom folder "{folder_name}" does not exist.')

    return f'./custom/{folder_name}/'

def main():
    custom_path = check_custom(sys.argv)
    game = SpaceInvaders((600, 600), custom_path=custom_path)
    game.run()

if __name__ == '__main__':
    main()