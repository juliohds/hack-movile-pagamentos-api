from __config__ import path_load
import os
import pandas as pd


class e_master(object):
    def __init__(self):
        self.name = self.__class__.__name__

    def open(self):
        return pd.read_pickle(f"{path_load}\#{self.name}.pkl")


files = os.listdir(path_load)
files = [x for x in files if x not in ['__init__.py', '__pycache__']]
files = [str(x).replace('#', '').replace('.pkl', '') for x in files]

for sistema_desc in files:
    globals()[sistema_desc] = e_master()
    globals()[sistema_desc].name = sistema_desc

print('Biblioteca de arquivos importada!')
