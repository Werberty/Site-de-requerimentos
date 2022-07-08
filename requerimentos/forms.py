from dataclasses import fields
from wsgiref.validate import validator

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

    def clean_especificar(self):
        data = self.cleaned_data["especificar"]
        if len(data) < 10:
            raise forms.ValidationError(
                'Campo possui menos que 10 caracteres.')
        return data

    def clean_justificar(self):
        data = self.cleaned_data["justificar"]
        if len(data) < 10:
            raise forms.ValidationError(
                'Campo possui menos que 10 caracteres.')
        return data

    def clean_matricula(self):
        data = self.cleaned_data["matricula"]
        try:
            data = int(data)
        except:
            raise forms.ValidationError('Valido somente números.')
        return data
