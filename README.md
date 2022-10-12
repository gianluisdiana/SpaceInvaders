![SpaceInvadersDeluxePoster](./images/poster.jpg)

# Space Invaders
* author: Gian Luis Bolivar Diana
* email: _gianluisbolivar1@gmail.com_

## How to play
* **Left arrow key** - Move the spaceship to the left
* **Right arrow key** - Move the spaceship to the right
* **Space bar** - Shoots

## Set up
The `main` file is located in the src folder, to start the program, execute the following command:
```BASH
python3 ./src/main.py
```
**IMPORTANT**: To run the game you must have installed the Python interpreter and the PyGame module, if you don't,
use this link to go to the official [Python website], and this one for the [PyGame module].

## Aditional flags:
  * ### Custom configuration
    If you want to use custom images, create a folder inside the **custom** one with the name you like, then, execute the program with the `--custom` flag and the name of the folder you created.
    ```BASH
    python3 ./src/main.py --custom my_custom_folder
    ```
  * ### CRT effect
    In order to display the CRT effect in the screen, we must execute our **main** file with the `--retro` flag activated.
    ```BASH
    python3 ./src/main.py --retro
    ```

## Directory Structure
```
  .
  ├── audio          # The audio played in the game
  ├── custom         # Custom configuration folders
  │   └── example          # Contain the wished config
  ├── fonts          # The fonts used to display text
  ├── images         # All the images that will be drawed
  │   └── aliens           # The images of the enemies
  └── src            # Game implementation
```

## References:
* [PyGame documentation](https://www.pygame.org/docs/)
* [Tutorial based](https://github.com/clear-code-projects/Space-invaders)
* [Github repository](https://github.com/gianluisdiana/SpaceInvaders)

[Python website]: <https://www.python.org/downloads/>
[PyGame module]: <https://www.pygame.org/download.shtml>