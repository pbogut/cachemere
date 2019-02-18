from .PickleDriver import PickleDriver

def start(name, driver='pickle', autosave=False):
    if driver == 'pickle':
        return PickleDriver(name, autosave=autosave)
