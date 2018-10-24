import pygame as pg
from pygame.math import Vector2 as vect2d
from laylib import DefaultEngine
from random import randint, uniform


"""
All settings:
"""
FPS = 60
WIDTH = 600
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Engine(DefaultEngine):
    """Short summary.

    Engine example: animation of rectangle with keyboard.
    Use arrows keys and Return to move bodies.
    - This class inherit from the DefaultEngine.
    """

    def __init__(self):
        super().__init__()
        self.new_demo()

    def update(self):
        self.all_sprites.update(self.dt)
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def new_demo(self):
        for _ in range(1000):
            size = randint(1, 5)
            self.all_sprites.add(Body((size, size), (WIDTH / 2, HEIGHT / 2)))
        self.playing = True


class Body(pg.sprite.Sprite):
    """
    Basic body for test
    """

    BODY_VEL = 180.0

    def __init__(self, size, pos):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vect2d(pos)
        self.rect.center = self.pos
        self.vel = vect2d(0.0, 0.0)

    def update(self, dt):
        """ this will update Body """
        keys = pg.key.get_pressed()
        rnd_speed = uniform(-self.BODY_VEL, -self.BODY_VEL * 3.0)
        if keys[pg.K_LEFT]:
            self.vel.x = rnd_speed
        if keys[pg.K_RIGHT]:
            self.vel.x = -rnd_speed
        if keys[pg.K_UP]:
            self.vel.y = rnd_speed
        if keys[pg.K_DOWN]:
            self.vel.y = -rnd_speed
        if keys[pg.K_RETURN]:
            self.pos = (WIDTH / 2, HEIGHT / 2)

        self.pos += self.vel * dt
        self.rect.center = self.pos
        bondary_limit(self.pos)
        self.vel = vect2d(0.0, 0.0)


def bondary_limit(position):
    """keep any object inside the screen"""

    if position.x < 0:
        position.x += WIDTH
    elif position.x > WIDTH:
        position.x -= WIDTH
    if position.y < 0:
        position.y += HEIGHT
    elif position.y > HEIGHT:
        position.y -= HEIGHT
