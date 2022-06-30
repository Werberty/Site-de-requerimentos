from django.http import HttpResponse
from django.shortcuts import render

from requerimentos.forms import formRequerimento


def home(request):
    form = formRequerimento()
    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })


def historico(request):
    return render(request, 'requerimentos/pages/historico.html')


def solicita_requerimento(request):
    if request.method == 'POST':
        form = formRequerimento(request.POST)
        if form.is_valid():
            form = formRequerimento()
            form.save()
            return render(request, 'requerimentos/pages/home.html', context={
                'form': form
            })

        return render(request, 'requerimentos/pages/home.html', context={
            'form': form
        })
