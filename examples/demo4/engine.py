import pygame as pg
from pygame.math import Vector2 as vect2d
from laylib import DefaultEngine
from random import randint
from random import uniform


RAIN_DENSITY = 450
MOON_POS = (190, 115)
DROP_LENGTH = 45
MIN_SPEED = 27.0
MAX_SPEED = 62.0
RAIN_LIFE = 1200
BLACK = (0, 0, 0)
COLOR_RAIN = (randint(200, 255),
              randint(1, 30),
              randint(200, 255))

MOON_COLOR = (255, 210, 255)

SHADOW_MINPOS = MOON_POS[0]
SHADOW_MAXPOS = 300


class Engine(DefaultEngine):
    """ Short summary.
    Main CLASS example: Demo rainy night, using laylib.
    This demo shows how to use laylib when you have no resource file to load
    and how to manage the main engine in any development context.

    (see the main file)
    """

    def __init__(self):
        super().__init__()
        self.setup()

    def update(self):
        # update the shadow
        self.shadow_moon.update(self.dt)
        if self.shadow_moon.x <= SHADOW_MINPOS:
            self.shadow_moon.x = SHADOW_MAXPOS
        # update drops
        for drop in self.rain:
            if drop.is_dead():
                self.rain.remove(drop)
                self.rain.append(self.new_drop(
                    uniform(RAIN_LIFE / 4.0, RAIN_LIFE)))

            drop.update(self.dt)

    def draw(self):
        self.screen.fill(BLACK)
        self.moon.draw(self.screen)
        self.shadow_moon.draw(self.screen)
        for drop in self.rain:
            drop.draw(self.screen)
        pg.display.update()

    # set up the demo
    def setup(self):
        self.rain = []
        self.playing = True
        # create rain's drops
        for _ in range(RAIN_DENSITY):
            self.rain.append(self.new_drop(
                uniform(RAIN_LIFE / 4.0, RAIN_LIFE)))
        # create moons
        self.moon = Moon(MOON_POS, (0, 0), MOON_COLOR, 48)
        self.shadow_moon = Moon(MOON_POS, (-0.7, 0), BLACK, 63)
        # rescale in laylib time unit to 100.0
        self.time_unit = 100.0

    @ staticmethod
    def new_drop(duration):

        pos = (uniform(0, 600), -DROP_LENGTH)
        vel = (0.0, uniform(MIN_SPEED, MAX_SPEED))
        color = (randint(200, 255),
                 randint(1, 80),
                 randint(200, 255))

        return Rain(pos, vel, color, duration)


class Rain(object):

    def __init__(self, pos, vel, color, duration):
        self.x, self.y = pos
        self.vel = vect2d(vel)
        self.color = color
        self.duration = duration
        self.startTime = pg.time.get_ticks()

    def update(self, dt):
        # update the move of drops
        self.x += self.vel.x * dt
        self.y += self.vel.y * dt

    def draw(self, screen):
        pg.draw.line(screen, self.color, (self.x, self.y),
                     (self.x + 5, self.y + uniform(DROP_LENGTH /
                                                   4.5, DROP_LENGTH * uniform(0.5, 1.9))))

    def is_dead(self):
        """
        tell if the elapsed time of particle's
        life is greater than duration or not """
        return pg.time.get_ticks() - self.startTime > self.duration


class Moon(object):

    def __init__(self, pos, vel, color, r):
        self.x, self.y = pos
        self.vel = vect2d(vel)
        self.color = color
        self.radius = r

    def update(self, dt):
        # update the move of moon
        self.x += self.vel.x * dt

    def draw(self, screen):
        pg.draw.circle(screen, self.color,
                       (int(self.x), int(self.y)), self.radius)
