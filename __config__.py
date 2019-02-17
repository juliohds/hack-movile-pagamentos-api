import pickle
from os import path
import pandas as pd

ajusta_coluna = pd.set_option("display.max_columns", 100)
ajusta_largura = pd.set_option('display.width', 150)

path = path.dirname(__file__)
path_app = fr'{path}\app'
path_data = fr'{path}\data'
path_extract = fr'{path_data}\extract'
path_load = fr'{path_data}\load'


def save_obj(obj, name):
    with open(f'{path_extract}\{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(f'{path_extract}\{name}.pkl', 'rb') as f:
        return pickle.load(f)
