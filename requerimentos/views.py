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
    if form.is_valid():
        form.save()
    else:
        return HttpResponse('ERRO')

    return render(request, 'requerimentos/pages/home.html', context={
        'form': form
    })
