
"""
Demo 3: Resources file example
------------------------------

# Creating the resources file:

This example explains how to create a persistence Layer
(resources.bin file) that contains the whole data structure
of all your resources.

1 - in your project create a folder (in our example the folder is: 'data')
add all your resources (images, fonts, sounds..) on this folder.

2 - on your main file call the function auto_save(true).
Once the file resources.bin is created on your data folder you
don't need this function call anymore except if you add more resources
to your folder and you need to update the resources.bin file.
"""

from laylib import Environment
from engine import Game
from laylib.resources import Resources


def auto_save(enabled=False):
    res = Resources('data')
    if enabled:
        res.save('resources.bin')


def main():
    # automatic creation of the resources file
    auto_save(True)
    # setting up the env
    game = Environment(800, 600, False, 'Resources Example')
    # now we are loading resources
    game.load_complete(Game(), 'data', 'resources.bin')
    game.gInstance.main_loop()
    game.destroy()


if __name__ == '__main__':
    main()
