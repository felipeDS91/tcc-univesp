from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .forms import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MovMensalistaForm,
    MensalistaForm
)

# Create your views here.


def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)


# Get a form, verify if is valid, save and redirect to app core_lista_pessoas
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()        
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()        
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def lista_mov_rotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rotativos':mov_rotativos, 'form':form}
    return render(request, 'core/lista_mov_rotativos.html', data)


def mov_rotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()        
    return redirect('core_lista_mov_rotativos')


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas':mensalistas, 'form':form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()        
    return redirect('core_lista_mensalistas')


def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas':mov_mensalistas, 'form':form}
    return render(request, 'core/lista_mov_mensalistas.html', data)


def mov_mensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()        
    return redirect('core_lista_mov_mensalistas')
