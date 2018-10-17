import pygame
import pytest


@pytest.mark.skip(reason="unskip this test if you're not using travis CI.")
def test_environment_class():
    # test if we had display
    assert pygame.display.get_init() == 1
    # the font
    assert pygame.font.get_init() == 1
    # see if the mixer return a list or a none obj.
    assert pygame.mixer.get_init() is not None


# this function will be tested with resources module cuz
# it just loads resources and set the main instance of the game.
@pytest.mark.skip(reason="will be tested with resources module.")
def test_load_complete():
    # set the main instance of the game to test destroy env function
    pass


@pytest.mark.skip(reason="will be tested with resources module.")
def test_destroy():
    pass
