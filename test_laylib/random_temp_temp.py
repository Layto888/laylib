import math
from pygame.math import Vector2 as vect2d


def rotate(v, angle):
    """ rotates a point p around the point origin."""
    vector = ((v.x * math.cos(angle) - v.y * math.sin(angle)),
              (v.x * math.sin(angle) + v.y * math.cos(angle)))
    return vector


x = vect2d(2.5, 1.1)
print(rotate(x, 0.0))
