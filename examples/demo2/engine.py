import pygame as pg
from pygame.math import Vector2 as vect2d
from laylib import DefaultEngine
from random import randint
from random import triangular
from random import uniform


"""
Parameters:
1. The number of particles
2. Number of special particles (With longer lifetime)
3. How many normal particles will be generated to generate one special particle
4. speed of particles on move
5. the duration of each particle between creation and death
6. the radius of each particle
7. the field of generated particle [0 ~ 100]
8. the particles colors.
9. background color
"""

PARTICLES_NUM = 2100
SPECIAL_PARTICLES_NUM = 100
CYCLE_NRML_PARTICLES = 70
X_MAX_SPEED = 300.0
Y_MAX_SPEED = 290.0
PARTICLE_DURATION = 59
PARTICLE_RADIUS = 1.2
THIKNESS = 0
COLOR_RANGE = (40, 255)
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
        self.cp = 0

    def update(self):
        # update all the group
        for particle in self.particles:
            if particle.is_dead():
                # remove the dead particles
                self.particles.remove(particle)
                # here append new particle to replace the dead one
                if self.cp < CYCLE_NRML_PARTICLES:

                    # Normal particles
                    self.particles.append(
                        self.new_particle(
                            pg.mouse.get_pos(), uniform(PARTICLE_DURATION / 3.0, PARTICLE_DURATION * 3.0)))
                    self.cp += 1
                else:
                    # specials particles : long lifetime duration
                    self.particles.append(
                        self.new_particle(
                            pg.mouse.get_pos(), uniform(PARTICLE_DURATION * 9.0, PARTICLE_DURATION * 20.0)))
                    self.cp = 0
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
            self.particles.append(self.new_particle(
                pg.mouse.get_pos(), uniform(PARTICLE_DURATION / 3.0, PARTICLE_DURATION * 3.0)))
        for _ in range(SPECIAL_PARTICLES_NUM):
            self.particles.append(self.new_particle(
                pg.mouse.get_pos(), uniform(PARTICLE_DURATION * 9.0, PARTICLE_DURATION * 20.0)))

    @staticmethod
    def new_particle(old_pos, duration):

        pos = (old_pos[0] + uniform(-THIKNESS, THIKNESS * 2),
               old_pos[1] + uniform(-THIKNESS, THIKNESS * 0.5))
        vel = (uniform(-X_MAX_SPEED, X_MAX_SPEED),
               uniform(-Y_MAX_SPEED, Y_MAX_SPEED))

        radius = triangular(0.5, PARTICLE_RADIUS, 0.4)
        choice1 = old_pos[0] % 255
        choice3 = old_pos[1] % 255
        choice2 = randint(0, 255)
        color = (choice1, choice2, choice3)
        return Particle(pos, vel, int(radius), color, duration)


class Particle(object):
    """
    particle class
    """

    def __init__(self, pos, vel, radius, color, duration):
        self.x, self.y = pos
        self.vel = vect2d(vel)
        self.radius = radius
        self.color = color
        self.duration = duration
        self.startTime = pg.time.get_ticks()

    def update(self, dt):
        # update the move of particles
        self.x += self.vel.x * dt
        self.y += self.vel.y * dt
        self.x = int(self.x)
        self.y = int(self.y)

    def draw(self, screen):
        pg.draw.circle(screen, self.color,
                       (int(self.x), int(self.y)), self.radius, 0)

    def is_dead(self):
        """
        tell if the elapsed time of particle's
        life is greater than duration or not """
        return pg.time.get_ticks() - self.startTime > self.duration
