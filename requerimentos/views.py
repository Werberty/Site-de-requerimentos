from django.shortcuts import render


def home(request):
    return render(request, 'requerimentos/pages/home.html')


def historico(request):
    return render(request, 'requerimentos/pages/historico.html')
