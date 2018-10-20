# test module default_engine.py
import pytest
import logging
import os
import inspect
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from laylib import default_engine

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

"""
@pytest.fixture
def surface_env(scope="function"):
    pg.init()
    if not pg.display.get_init():
        logging.info('unable to init display pygame')
    set_env = pg.display.set_mode((200, 200))
    yield set_env
    # pg.quit()
"""


class _ObjClass(default_engine.DefaultEngine):
    pass


@pytest.fixture
def class_default_engine():
    new_class = _ObjClass()
    return new_class


@pytest.mark.skip(reason="unskip this test if you're not using travis CI.")
def test_surface_env(surface_env):
    # the screen should not be none.
    assert surface_env is not None
    assert surface_env.get_size() == (200, 200)


def test_default_engine_attr(class_default_engine):
    assert isinstance(class_default_engine, default_engine.DefaultEngine)
    assert class_default_engine.running is True
    assert class_default_engine.playing is False
    assert class_default_engine._time_unit == 1000.0


def test_time_setget(class_default_engine):
    class_default_engine.time_unit = 20.0
    assert class_default_engine.time_unit == 20.0
    class_default_engine.time_unit = -50.0
    assert class_default_engine.time_unit == 1000.0


@pytest.mark.skip(reason="We can't exit the main_loop this way")
def test_delta_time_main_loop(class_default_engine):
    pass


@pytest.mark.skip(reason="will not be tested. User interaction")
def test_event_listener():
    pass


@pytest.mark.skip(reason="will be tested with resources module.")
def test_load_game():
    pass


def test_destroy_game(class_default_engine):
    class_default_engine.destroy_game()
    assert class_default_engine.all_sprites is not None
    assert class_default_engine.img is None
    assert class_default_engine.snd is None
    assert class_default_engine.fnt is None
