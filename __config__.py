import pickle
from os import path


path = path.dirname(__file__)
path_app = path + r'\app'
path_data = path + r'\data'
path_extract = path_data + r'\extract'
path_load = path_data + r'\load'


def save_obj(obj, name):
    with open(f'{path_extract}\{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(f'{path_extract}\{name}.pkl', 'rb') as f:
        return pickle.load(f)
