import pygame as pg
from pygame.math import Vector2 as vect2d
from laylib import DefaultEngine
from random import randint
from random import uniform


"""
Parameters:
1. The number of particles
2. speed of particles on move
3. the duration of each particle between creation and death
4. the radius of each particle
5. the field of generated particle
6. the particles colors.
7. background color
"""

PARTICLES_NUM = 1100
X_MAX_SPEED = 335.0
Y_MAX_SPEED = 530.0
PARTICLE_DURATION = 380
PARTICLE_RADIUS = 5
THIKNESS = 2.0
COLOR_RANGE = (80, 255)
BLACK = (0, 0, 0)


class Engine(DefaultEngine):
    """ Short summary.
    Engine example: A mini particles system, using laylib.
    This demo shows how to use laylib when you have no resource file to load
    (see the main file)
    """

    def __init__(self):
        super().__init__()
        self.new_demo()

    def update(self):
        # update all the group
        for particle in self.particles:
            if particle.is_dead():
                # remove the dead particles
                self.particles.remove(particle)
                # here append new particle to replace the dead one
                self.particles.append(
                    self.generate_particle(pg.mouse.get_pos()))

            particle.update(self.dt)

    def draw(self):
        self.screen.fill(BLACK)
        for particle in self.particles:
            particle.draw(self.screen)
        pg.display.update()

    def new_demo(self):
        self.particles = []
        self.playing = True
        for _ in range(PARTICLES_NUM):
            self.particles.append(self.generate_particle(pg.mouse.get_pos()))

    @staticmethod
    def generate_particle(old_pos):
        pos = (old_pos[0],
               old_pos[1])
        vel = (uniform(-X_MAX_SPEED, X_MAX_SPEED),
               uniform(-Y_MAX_SPEED, Y_MAX_SPEED))
        radius = uniform(1, PARTICLE_RADIUS)
        choice = randint(*COLOR_RANGE)
        color = (randint(*COLOR_RANGE), randint(*COLOR_RANGE), choice)
        return Particle(pos, vel, int(radius), color)


class Particle(object):
    """
    particle class
    """

    def __init__(self, pos, vel, radius, color):
        self.x, self.y = pos
        self.vel = vect2d(vel)
        self.radius = radius
        self.color = color
        self.duration = uniform(PARTICLE_DURATION / 3, PARTICLE_DURATION)
        self.startTime = pg.time.get_ticks()

    def update(self, dt):
        # update the move of particles
        self.x += self.vel.x * dt
        self.y += self.vel.y * dt
        self.x = int(self.x)
        self.y = int(self.y)

    def draw(self, screen):
        pg.draw.circle(screen, self.color,
                       (self.x, self.y), self.radius, 0)

    def is_dead(self):
        """
        tell if the elapsed time of particle's
        life is greater than duration or not """
        return pg.time.get_ticks() - self.startTime > self.duration
