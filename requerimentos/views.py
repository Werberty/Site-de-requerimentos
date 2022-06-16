from django.shortcuts import render


def home(request):
    return render(request, 'requerimentos/pages/home.html')


def solicitacao(request):
    return render(request, 'requerimentos/pages/solicitacao.html')
