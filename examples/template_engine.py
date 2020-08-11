"""
Template-file for the main engine of your pygame project.
Author:
Date:
summary :
"""

import pygame as pg
from laylib import DefaultEngine

BLACK = (0, 0, 0)
FPS = 30.0


class Engine(DefaultEngine):
    """ Short summary.

    """

    def __init__(self):
        super().__init__()
        self.setup()

    def update(self):
        """ Code to update all classes : 
        the global behavior should be written here.


        """
        pass

    def draw(self):
        self.screen.fill(BLACK)
        """ Code to draw all classes
        

        """
        pg.display.update()

    # init engine or set up environement

    def setup(self):
        self.playing = True
        # rescale in laylib time unit to 100.0 as example
        self.time_unit = 100.0
        self.fps = FPS
        """
        rest of init code
        """
