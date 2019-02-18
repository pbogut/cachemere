import os
import pickle


class PickleDriver:
    def __init__(self, name, autosave=False):
        self.name = name
        self.autosave = autosave

        storage_dir = os.getenv('HOME') + '/.cache/cachemere/drivers/pickle/'
        try:
            os.makedirs(storage_dir)
        except:
            pass

        self.file_name = storage_dir + self.name

        self.data = {}
        if os.access(self.file_name, os.W_OK):
            fd = open(self.file_name, 'rb')
            self.data = pickle.load(fd)
            fd.close()

    def set(self, key, value):
        self.data[key] = value
        if self.autosave:
            self.save()
            return self

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]
        else:
            return default

    def save(self):
        fw = open(self.file_name, 'wb')
        pickle.dump(self.data, fw)
        fw.close()
