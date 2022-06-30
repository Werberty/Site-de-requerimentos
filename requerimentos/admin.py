from django.contrib import admin
from .models import Requerimento


# class TipoAdmin(admin.ModelAdmin):
#     ...


@admin.register(Requerimento)
class RequerimentoAdmin(admin.ModelAdmin):
    ...
