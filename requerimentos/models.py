from unicodedata import name
from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Requerimento(models.Model):
    requerente = models.CharField(max_length=20)
    matricula = models.CharField(max_length=14)
    data_nascimento = models.CharField(max_length=10)
    naturalidade = models.CharField(max_length=65)
    filiacao = models.CharField(max_length=65)
    curso = models.CharField(max_length=65)
    periodo = models.CharField(max_length=10)
    turno = models.CharField(max_length=65)
    telefone = models.CharField(max_length=65)
    especificar = models.CharField(max_length=65)
    justificar = models.CharField(max_length=65)
    feito = models.BooleanField(default=False)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
