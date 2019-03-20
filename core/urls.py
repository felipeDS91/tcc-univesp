from django.urls import path, re_path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_mov_rotativos,
    lista_mensalistas,
    lista_mov_mensalistas,
    pessoa_novo,
    veiculo_novo,
    mov_rotativos_novo,
    mov_mensalistas_novo,
    mensalista_novo,
    pessoa_update,
    veiculo_update
)
urlpatterns = [
    re_path(r'^$', home, name='core_home'), 

    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),

    re_path(r'^mov-rot-list/$', lista_mov_rotativos, name='core_lista_mov_rotativos'),
    re_path(r'^mov-rot-novo/$', mov_rotativos_novo, name='core_mov_rotativos_novo'),
    
    re_path(r'^mov-mensalistas/$', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    re_path(r'^mov-mensalista-novo/$', mov_mensalistas_novo, name='core_mov_mensalistas_novo'),
    
    re_path(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo')
    
]