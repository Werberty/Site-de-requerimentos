from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('solicita_requerimento/', views.solicita_requerimento, name='solicita_requerimento'),
    path('historico/', views.historico, name='historico'),
]
