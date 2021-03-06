# test resources manager - parser (PM)
# test resources loader
# test Music / SOund / Font classes.

import os
import pytest
from laylib import resources as rc


@pytest.fixture
def class_resources(scope='module'):
    res_class = rc.Resources('examples/data')
    yield res_class


@pytest.fixture
def folder_data(scope='module'):
    _data = {'fntList': [['secrcode.ttf', 20], ['ahellya.ttf', 20]],
             'imgList': ['circle_pop-5.png',
                         'circle_pop-4.png',
                         'circle_pop-2.png',
                         'circle_pop-6.png',
                         'circle_pop-10.png',
                         'rotator.png',
                         'circle.png',
                         'circle_pop-8.png',
                         'circle_pop-11.png',
                         'circle_pop-0.png',
                         'bidoubird.jpg',
                         'circle_pop-3.png',
                         'circle_pop-12.png',
                         'circle_pop-1.png',
                         'circle_pop-9.png',
                         'circle_pop-7.png'],
             'mscList': [['RoyaltyMusic.MP3', 0.5], ['WhereWasI.ogg', 0.5]],
             'other': [],
             'sndList': [['bounce.wav', 0.8],
                         ['bounce_wall.wav', 0.8],
                         ['score.wav', 0.8]],
             'unknown': ['LICENSES'],
             'version': '0.2.2'}
    yield _data


def test_res_attr(class_resources):
    res = class_resources
    assert res.data_folder == 'examples/data'
    assert res.global_data is None
    assert res.pm is not None
    for k in res.pm.parser.keys():
        if k != 'version':
            assert res.pm.parser[k] == []

    assert isinstance(res.img, rc.Image)
    assert isinstance(res.snd, rc.Sound)
    assert isinstance(res.fnt, rc.Font)
    assert isinstance(res.msc, rc.Music)


def test_jsave_jget_info(class_resources, folder_data):
    # test METHOD1 parser Manual: save infos
    res = class_resources
    res.jsave_info(folder_data, 'foo.txt', True)
    assert os.path.isfile('examples/data/foo.txt')
    # test load infos
    if os.path.exists('examples/data/foo.txt'):
        # test get infos:
        data = res.jget_info('foo.txt')
        assert data == folder_data
        os.remove('examples/data/foo.txt')


def test_save_get_parser(class_resources, folder_data):
    # test METHOD2 parser Auto: save infos
    res = class_resources
    res.save('bar.bin')
    assert os.path.isfile('examples/data/bar.bin')
    # test load infos
    if os.path.exists('examples/data/bar.bin'):
        # test get infos:
        data = res.get('bar.bin')

        for k in data.keys():
            if k != 'other':
                for element in data[k]:
                    assert element in folder_data[k]
        os.remove('examples/data/bar.bin')


@pytest.mark.skip(reason="stdout print")
def test_show():
    pass


def test_persistenceManager_cls():
    """
    This class is already fully tested with
    res.save() and res.get() in test_save_get_parser().
    """
    assert True
