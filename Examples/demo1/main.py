"""
Demo 01 Made with python and pygame
to test and improve the laylib-pygame framwork for fast game prototyping.
----
Author: Amardjia Amine
Date: 31/07/18
Github: ---

TODO: -
"""
from laylib import Environment
from engine import Engine
from settings import WIDTH, HEIGHT


def main():
    # init global environment
    demo = Environment(

        WIDTH,     # width
        HEIGHT,    # height
        False,     # full screen
        '2D Demo'  # window title
    )
    # load resources, set the game
    demo.load_complete(Engine(), 'data', 'resources.res')
    # play
    demo.gInstance.main_loop()
    # quit the game
    demo.destroy()


if __name__ == "__main__":
    main()
