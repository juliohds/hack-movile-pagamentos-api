import pickle
import os
import pandas as pd

ajusta_coluna = pd.set_option("display.max_columns", 100)
ajusta_largura = pd.set_option('display.width', 150)

path = os.path.dirname(__file__)
windows = False


def ajusta_path(par1, par2):
    if windows:
        return fr'{par1}\{par2}'
    else:
        return os.path.join(par1, par2)

path_app = ajusta_path(path, 'app')
path_data = ajusta_path(path, 'data')
path_extract = ajusta_path(path_data, 'extract')
path_load = ajusta_path(path_data, 'load')


def save_obj(obj, name):
    with open(f'{path_extract}\{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(f'{path_extract}\{name}.pkl', 'rb') as f:
        return pickle.load(f)
