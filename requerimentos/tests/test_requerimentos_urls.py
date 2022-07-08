from django.test import TestCase
from django.urls import reverse


class RequerimentosURLsTest(TestCase):
    def test_requerimento_home_url_is_correcty(self):
        url = reverse('home')
        self.assertEqual(url, '/home/')

    def test_requerimento_solicita_url_is_correcty(self):
        url = reverse('solicita_requerimento', kwargs={'id': 1})
        self.assertEqual(url, '/solicita_requerimento/1')

    def test_historico_url_is_correcty(self):
        url = reverse('historico')
        self.assertEqual(url, '/historico/')
