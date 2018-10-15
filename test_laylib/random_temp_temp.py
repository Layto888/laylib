import math
from pygame.math import Vector2 as vect2d


def rotate(v, angle):
    """ rotates a point p around the point origin."""
    vector = ((v.x * math.cos(angle) - v.y * math.sin(angle)),
              (v.x * math.sin(angle) + v.y * math.cos(angle)))
    return vector


x = vect2d(6.3, 1.5)
print(rotate(x, -8))
