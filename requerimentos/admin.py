from django.contrib import admin
from .models import Tipo, Requerimento


class TipoAdmin(admin.ModelAdmin):
    ...


@admin.register(Requerimento)
class RequerimentoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Tipo, TipoAdmin)
