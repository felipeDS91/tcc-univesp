from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
import csv

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

@login_required
def home(request):    
    data = {'viewName':'Início'}
    return render(request, 'core/index.html', data) # , context


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form, 'viewName':'Cadastro de Pessoas'}
    return render(request, 'core/lista_pessoas.html', data)


# Get a form, verify if is valid, save and redirect to app core_lista_pessoas
@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    data = {'form':form, 'viewName':'Novo Cadastro de Pessoas'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/new_insert.html', data)


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    data['viewName'] = 'Cadastro de Pessoas'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':pessoa, 'viewName':'Cadastro de Pessoas'})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form, 'viewName':'Cadastro de Veículos'}
    return render(request, 'core/lista_veiculos.html', data)


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    data = {'form':form, 'viewName':'Novo Cadastro de Veículo'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/new_insert.html', data)


@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    data['viewName'] = 'Cadastro de Veículos'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':veiculo, 'viewName':'Cadastro de Veículos'})


@login_required
def lista_mov_rotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rotativos':mov_rotativos, 'form':form, 'viewName':'Rotativos'}
    return render(request, 'core/lista_mov_rotativos.html', data)


@login_required
def mov_rotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    data = {'form':form, 'viewName':'Novo Movimento Rotativo'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/new_insert.html', data)


@login_required
def mov_rotativos_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form
    data['veiwName'] = 'Rotativos'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/update_mov_rotativo.html', data)


@login_required
def mov_rotativos_delete(request, id):
    mov_rotativos = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativos.delete()
        return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mov_rotativos, 'viewName':'Rotativos'})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas':mensalistas, 'form':form, 'viewName':'Cadastro de Mensalistas'}
    return render(request, 'core/lista_mensalistas.html', data)


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    data = {'form':form, 'viewName':'Novo Cadastro de Mensalista'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/new_insert.html', data)


@login_required
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    data['viewName'] = 'Cadastro de Mensalistas'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mensalista, 'viewName':'Cadastro de Mensalistas'})


@login_required
def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas':mov_mensalistas, 'form':form, 'viewName':'Movimento Mensalistas'}
    return render(request, 'core/lista_mov_mensalistas.html', data)


@login_required
def mov_mensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    data = {'form':form, 'viewName':'Novo Movimento Mensalista'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/new_insert.html', data)


@login_required
def mov_mensalistas_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    data['viewName'] = 'Movimento Mensalistas'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)


@login_required
def mov_mensalistas_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mov_mensalista, 'viewName':'Movimento Mensalistas'})

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename="relatorio_veiculos.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'Placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario, veiculo.cor
            ])

        return response