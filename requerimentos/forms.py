from dataclasses import fields

from django import forms

from .models import Requerimento

class formRequerimento(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = (
            'requerente',
            'matricula',
            'data_nascimento',
            'naturalidade',
            'filiacao',
            'curso',
            'periodo',
            'turno',
            'telefone',
            'tipo',
            'especificar',
            'justificar',
            'anexo',
        )
