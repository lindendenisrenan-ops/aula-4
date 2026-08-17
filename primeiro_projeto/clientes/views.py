from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    dados = {
        'mensagem' : ' Estamos na Index'
    }

    return render(request, 'clientes/index.html', dados)


def clientes(request):

    lista_clientes = [
        'Denis',
        'Carlos',
        'Giovani',
        'Carol',
        'Pedro',
    ]

    dados = {
        'clientes' : lista_clientes
    }

    return render(request, 'clientes/clientes.html', dados)


def sobre(request):
    return render(request, 'clientes/sobre.html')


def bye(request):
    return HttpResponse("Estamos na Bye")


def hello(request):
    return HttpResponse("Estamos na hello")


def excluir(request):
    return HttpResponse("Estamos na Excluir")
