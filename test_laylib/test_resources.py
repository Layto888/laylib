# test resources manager - parser (PM)
# test resources loader
# test Music / SOund / Font classes.

# TODO: with laylib the classes Sound/ Font/ MSC should
# return None in case of empty data.

import os
import pytest
from laylib import resources as rc


@pytest.fixture
def class_resources(scope="function"):
    res_class = rc.Resources('test_laylib/data_test')
    return res_class


@pytest.fixture
def folder_data(scope="function"):
    _data = {

        'mscList': [['RoyaltyMusic.MP3', 2.0]],
        'imgList': ['bird_800.jpg'],
        'sndList': [],
        'fntList': [['Rockout.otf', 20]],
        'version': '0.2.1',
        'other': ['bar.bin']
    }
    return _data


def test_res_attr(class_resources):
    res = class_resources
    assert res.data_folder == 'test_laylib/data_test'
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
    assert os.path.isfile('test_laylib/data_test/foo.txt')
    # test load infos
    if os.path.exists('test_laylib/data_test/foo.txt'):
        # test get infos:
        data = res.jget_info('foo.txt')
        assert data == folder_data
        os.remove('test_laylib/data_test/foo.txt')


def test_save_get_parser(class_resources, folder_data):
    # test METHOD2 parser Auto: save infos
    res = class_resources
    res.save('bar.bin')
    assert os.path.isfile('test_laylib/data_test/bar.bin')
    # test load infos
    if os.path.exists('test_laylib/data_test/bar.bin'):
        # test get infos:
        data = res.get('bar.bin')
        for k in data.keys():
            if k != 'other':
                assert data[k] == folder_data[k]
        os.remove('test_laylib/data_test/bar.bin')


@pytest.mark.skip(reason="stdout print")
def test_show():
    pass


def test_persistenceManager_cls():
    """
    This class is already fully tested with
    res.save() and res.get() in test_save_get_parser().
    """
    assert True
