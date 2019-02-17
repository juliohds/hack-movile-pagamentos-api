import os
from builtins import print
import pandas as pd
import datetime
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def modelo_knn():
    file = os.path.join('databases','database.csv')
    df = pd.read_csv(file,sep="\t")
    #  clean database

    print(df.columns)


    def calcula_idade(data_nascimento):
        ano, mes, dia = data_nascimento.split("-")
        d1 = datetime.datetime(int(ano), int(mes), int(dia))
        d2 = datetime.datetime.now()

        diff = d2 - d1

        days = diff.days
        years, days = days // 365, days % 365
        months, days = days // 30, days % 30

        seconds = diff.seconds
        hours, seconds = seconds // 3600, seconds % 3600
        minutes, seconds = seconds // 60, seconds % 60
        return years
        #print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))

    def nivela_idade(idade):
        if(idade <= 30):
            return 1
        else:
            if(idade >= 31 and idade <= 60):
                return 2
            else:
                return 3



    df['data_nascimento'] = df['data_nascimento'].apply(lambda x: calcula_idade(x))
    df['data_nascimento'] = df['data_nascimento'].apply(lambda x: nivela_idade(x))

    def sexo(sexo):
        if(sexo == 'M'):
            return 1
        else:
            return 2

    def estado(estado):
        if(estado == 'SP'):
            return 1
        else:
            return 2

    def qtd_historico(historico):
        if(historico < 5):
            return 1
        else:
            if(historico >=5 and historico >=7):
                return 2
            else:
                return 3

    def renda_mensal(renda):
        if(renda >= 1200):
            return 1
        else:
            if(renda >= 1201 and renda <= 5000):
                return 2
            else:
                return 3

    def estado_civil(estado):
        if (estado == 'S'):
            return 1
        else:
            return 2

    def numero_filhos(filhos):
        if(filhos == 0):
            return 1
        else:
            if(filhos >= 1 and filhos <= 3):
                return 2
            else:
                return 3

    def score(status):
        if(status == 'A'):
            return 1
        else:
            return 2

    df['sexo'] = df['sexo'].apply(lambda x: sexo(x))
    df['estado'] = df['estado'].apply(lambda x: estado(x))
    df['qtd_historico'] = df['qtd_historico'].apply(lambda x: qtd_historico(x))
    df['renda_mensal'] = df['renda_mensal'].apply(lambda x: renda_mensal(x))
    df['estado_civil'] = df['estado_civil'].apply(lambda x: estado_civil(x))
    df['filhos'] = df['filhos'].apply(lambda x: numero_filhos(x))
    df['score'] = df['score'].apply(lambda x: score(x))


    print(df.head())

    #  train and test on model using LeaveOneOut method
    Y = df['score']
    X = df.drop(columns=['score'])

    '''
    from sklearn.model_selection import LeaveOneOut
    loo = LeaveOneOut()
    print(loo.get_n_splits(X))
    #print(loo)
    for train_index, test_index in loo.split(X):
        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        #y_train, y_test = Y[train_index], Y[test_index]
        #print(X_train, X_test, y_train, y_test)
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(X_train, y_train)
    print(neigh.predict(X_test))
    #exemplo pegar a linha x

    return neigh.predict_proba([[1, 1, 2, 1, 2, 1, 1]])
