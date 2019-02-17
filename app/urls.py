from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^SolicitacaoEmprestimo', SolicitacaoEmprestimo.as_view(), name='SolicitacaoEmprestimo'),
    ]
