
from django.test import TestCase
from django.urls import resolve, reverse
from requerimentos import views


class RequerimentosViewsTest(TestCase):
    def test_requerimentos_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    def test_requerimentos_solicita_view_function_is_correct(self):
        view = resolve(reverse('solicita_requerimento', kwargs={'id': 1}))
        self.assertIs(view.func, views.solicita_requerimento)

    def test_requerimentos_historico_view_function_is_correct(self):
        view = resolve(reverse('historico'))
        self.assertIs(view.func, views.historico)
