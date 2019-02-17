df = pd.read_pickle('H:\MovileHack\data\extract\historico\historico_20190217010903.pkl')
df['id'] = df['cpf'].astype(str) + '_' + '20190217010903'
del df['cpf']
df.to_pickle('H:\MovileHack\data\extract\historico\historico_20190217010903.pkl')
