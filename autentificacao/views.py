from ast import Return

from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login(request):
    if request.method == 'GET':
        return render(request, 'autentificacao/login.html')
    else:
        user = get_user_model()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        username = user.objects.get(email=email)

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('/home')
        else:
            return HttpResponse('Invalido')


def logout(request):
    auth.logout(request)
    return render(request, 'autentificacao/login.html')
