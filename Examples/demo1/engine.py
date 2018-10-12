import pygame as pg
from random import randint
from laylib import DefaultEngine
from settings import (WIDTH, HEIGHT, NUM_CHAR_IMG, FPS)
from body import Body, Background


class Engine(DefaultEngine):
    """
    Engine game example:
    this is the Main class of your game as example.
    - Manage event, update and draw the whole demo.
    """

    def __init__(self):
        super().__init__()
        self.body = None
        self.all_sprites = pg.sprite.Group()
        # setting new delta time, we're dividing pg.time.get_ticks() by 500.0
        # the default value is 1000.0
        self.time_unit = 500.0
        print("time unit = {}".format(self.time_unit))

    def update(self):
        if not self.playing:
            self.new_demo()
        self.all_sprites.update(self.dt)
        self.clock.tick(FPS)

    def draw(self):

        self.all_sprites.draw(self.screen)
        self.res.fnt.render(
            self.fnt[0], 'Velocity body: {}'.format(self.body.vel), (10, 45)
        )
        self.res.fnt.render(
            self.fnt[0], "FPS: {:.2f}".format(self.clock.get_fps()), (10, 20)
        )
        self.res.fnt.render(
            self.fnt[0], "Dela time: {:.4f}".format(self.dt), (10, 70)
        )
        pg.display.flip()

    def new_demo(self):
        self.all_sprites.add(Background(self))

        for _ in range(NUM_CHAR_IMG):
            self.body = Body(self, (randint(0, WIDTH), HEIGHT))
            self.all_sprites.add(self.body)

        self.playing = True
