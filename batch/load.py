import pandas as pd
import os
from __config__ import path_extract, path_load


def reload():

    for tipo_arquivo in ['usuario', 'historico', 'transacao']:
        df_total = pd.DataFrame()
        for files in os.listdir(f'{path_extract}\{tipo_arquivo}'):
            df = pd.read_pickle(f'{path_extract}\{tipo_arquivo}\{files}')
            df_total = pd.concat([df, df_total])

        df_total.to_pickle(f'{path_load}\#{tipo_arquivo}.pkl')
