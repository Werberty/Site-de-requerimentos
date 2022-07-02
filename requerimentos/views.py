from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from requerimentos.forms import formRequerimento

from .models import Requerimento


@login_required(login_url='/auth/login')
def home(request):
    form = formRequerimento()
    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })


@login_required(login_url='/auth/login')
def historico(request):
    requerimentos = Requerimento.objects.all()
    return render(request, 'requerimentos/pages/historico.html', context={
        'requerimentos': requerimentos,
    })


@login_required(login_url='/auth/login')
def solicita_requerimento(request):
    form = formRequerimento(request.POST, request.FILES)

    if not form.is_valid():
        messages.add_message(request, messages.ERROR,
                             'Algum campo está preenchido incorreto.')
        form = formRequerimento(request.POST)
        return render(request, 'requerimentos/pages/home.html', context={
            'form': form
        })

    form.save()
    messages.add_message(request, messages.SUCCESS,
                         'Requerimento feito com sucesso!')
    form = formRequerimento()
    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })
