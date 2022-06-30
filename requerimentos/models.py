from unicodedata import name
from django.db import models

TURNOS = (
    ('m', 'Manhã'),
    ('t', 'Tarde'),
    ('n', 'Noite'),
    ('i', 'integral')
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


# class Tipo(models.Model):
#     nome = models.CharField(max_length=50, choices=TIPOS)

#     def __str__(self) -> str:
#         return self.nome


class Requerimento(models.Model):
    requerente = models.CharField(max_length=255)
    matricula = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=65)
    filiacao = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    periodo = models.CharField(max_length=35)
    turno = models.CharField(max_length=1, choices=TURNOS)
    telefone = models.CharField(max_length=65)
    especificar = models.TextField()
    justificar = models.TextField()
    feito = models.BooleanField(default=False)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    anexo = models.ImageField(
    upload_to='requerimento/anexo/%Y/%m/%d/', blank=True, default='')
    tipo = models.CharField(max_length=50, choices=TIPOS)

    def __str__(self) -> str:
        return self.tipo
