import pygame as pg
from pygame.math import Vector2 as vect2d
from settings import (BACKGROUND_IMG, WIDTH, HEIGHT, NUM_CHAR_IMG)
from random import randint

MAX_VEL = 50.0


class Body(pg.sprite.Sprite):

    """
    The body demo class is the player in the game
        This class contain an instance from the engine
        it's useful when the class use sound or image from
        the engine class.
    """

    def __init__(self, engine, pos=(0, 0)):
        super().__init__()
        self.image = engine.img[randint(0, NUM_CHAR_IMG)]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.vel = vect2d(0.0, 0.0)
        self.acc = vect2d(1.5, 0.5)
        self.rot = 0.0
        self.rot_vel = 0.0
        self.last_respawn = pg.time.get_ticks()

    def update(self, dt):
        """this will update Body """
        self.vel += self.acc * dt
        self.cap_velocity()
        self.pos += self.vel
        self.rect.center = self.pos
        bondary_limit(self.pos)

    def cap_velocity(self):
        """limit max speed """
        if self.vel.x > MAX_VEL:
            self.vel.x = MAX_VEL
        if self.vel.y > MAX_VEL:
            self.vel.y = MAX_VEL


class Background(pg.sprite.Sprite):
    def __init__(self, engine, pos=vect2d(0, 0)):
        super().__init__()
        self.image = engine.img[BACKGROUND_IMG]
        self.rect = self.image.get_rect()
        self.pos = pos


def bondary_limit(position):
    """
    keep any object inside the screen
    """
    if position.x < 0:
        position.x += WIDTH
    elif position.x > WIDTH:
        position.x -= WIDTH
    if position.y < 0:
        position.y += HEIGHT
    elif position.y > HEIGHT:
        position.y -= HEIGHT
