from django.urls import path, re_path
from django.urls import path
from .views import (
    home, 
    contato,
    servicos,
    sobre,
    planos,
)

urlpatterns = [
    re_path(r'^$', home, name='website_home'), 
    re_path(r'^contato$', contato, name='website_contato'), 
    path('servicos', servicos, name='website_servicos'), 
    path('sobre', sobre, name='website_sobre'), 
    path('planos', planos, name='website_planos'), 
  
]