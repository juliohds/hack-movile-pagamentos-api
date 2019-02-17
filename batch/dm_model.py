import data.load as _l
import pandas as pd
from __config__ import path_load


def reload():
    transacao = _l.transacao.open()
    usuario = _l.usuario.open()
    historico = _l.historico.open()

    qtde_historico = historico.groupby('id', as_index=False)['valor'].count()
    qtde_historico = qtde_historico.rename(columns={'valor': 'qtde_historico'})

    full_transacao = pd.merge(transacao, usuario, how='left', on='cpf')
    full_transacao = pd.merge(full_transacao, qtde_historico, how='left', on='id')

    full_transacao = full_transacao[['valor_emprestimo', 'data_nascimento', 'sexo', 'estado', 'qtde_historico']]

    full_transacao.to_pickle(f'{path_load}\#dm_model.pkl')


if __name__ == '__main__':
    reload()
