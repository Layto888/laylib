# test util.py module

import pytest
from laylib import util
from pygame.math import Vector2 as vect2d


class Body(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


@pytest.fixture
def null_body():
    return Body(0, 0, 0, 0)


@pytest.mark.parametrize("vector1, vector2, expected", [
    (vect2d(-1.0, 1.0), vect2d(-1.0, 1.0), 0.0),
    (vect2d(-2.1, 3.0), vect2d(1.0, -5.1), 8.672),
    (vect2d(-1.3, -2.0), vect2d(2.0, 1.3), 4.666)
])
def test_dist(vector1, vector2, expected):
    assert(util.dist(vector1, vector2) == pytest.approx(expected, 0.01))


@pytest.mark.parametrize("rad, expected", [
    (0, 0),
    (33.3, 1907.94),
    (0.81, 46.40)
])
def test_rad2deg(rad, expected):
    assert(util.rad2deg(rad) == pytest.approx(expected, 0.01))


@pytest.mark.parametrize("deg, expected", [
    (0, 0),
    (25.2, 0.43),
    (0.28, 0.0048)
])
def test_deg2rad(deg, expected):
    assert(util.deg2rad(deg) == pytest.approx(expected, 0.1))


# graphics stuffs : TODO -- test load image rot
@pytest.mark.skip(reason="no way of currently testing this")
def test_rotateDeg():
    pass
