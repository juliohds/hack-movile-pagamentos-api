import pickle
from os import path


# path = path.dirname(__file__)
path = r"H:\MovileHack\app"
path_data = path + r'\requests'
path_database = path + r'\database'


def save_obj(obj, name):
    with open(f'{path_data}\{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(f'{path_data}\{name}.pkl', 'rb') as f:
        return pickle.load(f)
