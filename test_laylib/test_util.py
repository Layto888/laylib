# test util.py module

import pytest
from laylib import util
from pygame.math import Vector2 as vect2d


@pytest.mark.parametrize("vector1, vector2, expected", [
    (vect2d(-1.0, 1.0), vect2d(-1.0, 1.0), 0.0),
    (vect2d(-2.1, 3.0), vect2d(1.0, -5.1), 8.672),
    (vect2d(-1.3, -2.0), vect2d(2.0, 1.3), 4.666)
])
def test_dist(vector1, vector2, expected):
    assert(dist(vector1, vector2) == pytest.approx(expected, 0.01))
