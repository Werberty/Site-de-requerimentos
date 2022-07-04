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
            'aluno',
        )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].widget.attrs.update(
            {'class': 'mask-data'})
        self.fields['telefone'].widget.attrs.update(
            {'class': 'mask-telefone'})
