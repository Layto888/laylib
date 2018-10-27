
"""
Demo 3: Resources file example
------------------------------

# Create the resources file:

This example explains how to create a persistence Layer
(resources.bin file) that contains and manages the whole data structure
of your resources.
"""

from laylib import Environment
from engine import Engine


def main():
    # setting up the env
    game = Environment(800, 600, False, 'Resources Example')
    # now we are loading resources
    game.load_complete(Engine(), '../data', 'resources.bin')
    game.gInstance.main_loop()
    game.destroy()


if __name__ == '__main__':
    main()
