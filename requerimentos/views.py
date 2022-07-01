from django.http import HttpResponse
from django.shortcuts import render

from requerimentos.forms import formRequerimento

from .models import Requerimento


def home(request):
    form = formRequerimento()
    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })


def historico(request):
    requerimentos = Requerimento.objects.all()
    return render(request, 'requerimentos/pages/historico.html', context={
        'requerimentos': requerimentos,
    })


def solicita_requerimento(request):
    form = formRequerimento(request.POST)
    if form.is_valid():
        form.save()
    else:
        return HttpResponse('ERRO')

    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })
