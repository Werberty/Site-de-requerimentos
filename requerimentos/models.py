from django.contrib.auth.models import User
from django.db import models


class Requerimento(models.Model):
    TURNOS = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('I', 'integral')
    )

    STATUS = (
        ('A', 'Em analise'),
        ('C', 'Concluido'),
        ('R', 'Rejeitado')
    )

    TIPOS = (
        ('2° via', '2° via'),
        ('Aproveitamento de disciplina', 'Aproveitamento de disciplina'),
        ('Matricula fora do prazo', 'Matricula fora do prazo'),
        ('Declaração', 'Declaração'),
        ('Diploma', 'Diploma'),
        ('Reabertura de matricula', 'Reabertura de matricula'),
        ('Segunda chamada', 'Segunda chamada'),
        ('Reingresso', 'Reingresso'),
        ('Trancamento de disciplina', 'Trancamento de disciplina'),
        ('Outros', 'Outros'),
    )

    aluno = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    requerente = models.CharField(max_length=255)
    matricula = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=65)
    filiacao = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    periodo = models.CharField(max_length=35)
    turno = models.CharField(max_length=1, choices=TURNOS)
    telefone = models.CharField(max_length=15)
    especificar = models.TextField()
    justificar = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    anexo = models.FileField(
        upload_to='requerimento/anexo/%Y/%m/%d/', blank=True)
    tipo = models.CharField(max_length=30, choices=TIPOS)

    def __str__(self) -> str:
        return self.tipo
