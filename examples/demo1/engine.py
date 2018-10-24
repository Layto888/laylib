import pygame as pg
from laylib import DefaultEngine

FPS = 25
POS_Y = 23
BLACK = (0, 0, 0)


class Engine(DefaultEngine):
    """
    resources management example:

    this is the Main class of your game as example.
    - In this first example we show how to manage your resources:
        1)- create a data folder and put all your resources into it.
        2)- create a class named engine or whatever, this class represents your main
        game engine.
        3)- the DefaultEngine class will automatically load and separate resources types for you:
            - self.img -> will contain the whole images
            - self.snd -> will contain the whole fx sounds (wav, midi...)
            - self.msc -> will contain the whole music (mp3, ogg)
            - self.fnt -> will contain the whole fonts (ttf..)

        4)- now we override the function DefaultEngine.draw to print the resources loaded as demo:
            - see the function DefaultEngine.draw()

     ANY need to manage resources manually:
     The thing is to put your resources in the data folder and they will be ready to use.

    """

    def __init__(self):
        super().__init__()
        self.text_pos = POS_Y
        self.new_demo()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.text_pos = POS_Y
        self.res.fnt.render(self.fnt[0], 'Loaded Data:', (1, 1))

        for res_file in self.res.pm.parser:
            for data in self.res.pm.parser[res_file]:
                if res_file != 'version':
                    self.res.fnt.render(
                        self.fnt[0], '{}: {}'.format(
                            res_file, data), (1, self.text_pos)
                    )
                    self.text_pos += POS_Y

        pg.display.flip()

    def new_demo(self):
        self.playing = True
