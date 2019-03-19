from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.


def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)

