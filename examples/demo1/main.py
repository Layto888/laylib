"""
Demo 01 Made with python and pygame
to test and improve the laylib-pygame framework for fast game prototyping.
----
Author: Amardjia Amine
Date: 20/10/18
Github: ---

- This demo shows how the Resources manager loads and
  separates the different data and their associated variables.

  All resources are showed in the terminal after running your program.
"""

from laylib import Environment
from engine import Engine
import sys


def main():
    # init global environment
    demo = Environment(

        800,       # width
        600,       # height
        False,     # full screen
        '2D Demo'  # window title
    )
    # load resources, set the game
    demo.load_complete(Engine(), '../data')
    # play
    demo.gInstance.main_loop()
    # quit the game
    demo.destroy()


if __name__ == "__main__":
    sys.exit(main())
