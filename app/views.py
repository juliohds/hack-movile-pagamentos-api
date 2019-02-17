from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, timedelta, datetime
import pandas as pd
import pickle
import random
from __config__ import save_obj, path_database
import json


delay = 1
d0 = date.today() - timedelta(days=1+delay)
d30 = (date.today() - timedelta(days=31+delay))
d90 = (date.today() - timedelta(days=91+delay))

# full_devedor = pd.read_pickle(r'\\' + ip['ip_thanus_fonte'] + r"\ProjetosDW\data\load\#devedor.pkl")


class SolicitacaoEmprestimo(APIView):
    def post(self, request):
        dicio = {}

        try:
            ''' salvar json '''
            body_dict = json.loads(str(request.body, encoding='utf-8'))
            id = body_dict['usuario']['cpf'] + '_' + datetime.now().strftime('%Y%m%d%H%M%S')
            save_obj(body_dict, id)

            df = pd.DataFrame.from_dict(body_dict['transacao'], orient='index')
            df['cpf'] = id
            df.to_pickle(f'{path_database}/#transacao.pkl')
            del df

            df = pd.DataFrame.from_dict(body_dict['usuario'], orient='index')
            df.to_pickle(f'{path_database}/#usuario.pkl')
            del df

            df = pd.DataFrame.from_dict(body_dict['historico'], orient='columns')
            df['cpf'] = int(save_obj['usuario']['cpf'])
            df.to_pickle(f'{path_database}/#historico.pkl')
            del df

            dicio['flag_aprovacao'] = random.randint(0, 1)

            if len(dicio) > 10000:
                dicio = {'status': 'limit exceeded', 'dados': ''}
            else:
                dicio = {'status': 'ok', 'dados': dicio}

        except:
            dicio = {'status': 'empty', 'dados': ''}

        return Response(data=dicio, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'app/home.html')
