import os
import pprint
import pickle


class PersistenceManager(object):
    """
    Persistence Manager:  automate the creation of a persistence layer for data
    - save and parse
    - load the persitence layer and return the data structure
    - The file is created into a binary format using pickle module.
    """
    __version = 0.4

    # class constants:
    IMAGE_TYPE = ('bmp', 'jpg', 'png', 'jpeg', 'tiff', 'gif', 'ico')
    MUSIC_TYPE = ('mp3', 'wma')
    FX_TYPE = ('ogg', 'wav')
    FONT_TYPE = ('ttf', 'otf', 'ttc')
    # theses values could be edited directly in the persistence file.
    DEFAULT_FX_VOLUME = 0.8
    DEFAULT_MUSIC_VOLUME = 2.0
    DEFAULT_FONT_SIZE = 25

    def __init__(self, folder='data'):
        self.parser = {
            'version': str(self.__version),
            'imgList': [],
            'sndList': [],
            'mscList': [],
            'fntList': [],
            'other': []
        }
        self.pp = pprint.PrettyPrinter(indent=4)
        self.files_list = os.listdir(folder)
        self.folder = folder

    def show(self):
        """
        show the content of parser
        """
        if self.parser:
            self.pp.pprint(self.parser)
        else:
            print(self)

    def _create_parserGroup(self):
        """ set the group list """
        for file in self.files_list:
            name, ext = file.split('.')

            if ext in self.IMAGE_TYPE:
                self.parser["imgList"].append(file)
            elif ext in self.MUSIC_TYPE:
                conf_file = [file, self.DEFAULT_MUSIC_VOLUME]
                self.parser["mscList"].append(conf_file)
            elif ext in self.FX_TYPE:
                conf_file = [file, self.DEFAULT_FX_VOLUME]
                self.parser["sndList"].append(conf_file)
            elif ext in self.FONT_TYPE:
                conf_file = [file, self.DEFAULT_FONT_SIZE]
                self.parser["fntList"].append(conf_file)
            else:
                self.parser["other"].append(file)

    def resources_get(self, persistence_file):
        """ load binary """
        with open(persistence_file, 'rb') as fp:
            data = pickle.load(fp)
        return data

    def resources_save(self, persistence_file):
        """ automate saving binary """
        self._create_parserGroup()
        with open(persistence_file, 'wb') as fp:
            pickle.dump(self.parser, fp, pickle.HIGHEST_PROTOCOL)


pm = PersistenceManager('data')
data = pm.resources_save('resources.res')
