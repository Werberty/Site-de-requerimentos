from django.contrib import admin

from .models import Requerimento

# class TipoAdmin(admin.ModelAdmin):
#     ...


class RequerimentoAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'requerente',
        'data_solicitacao',
        'curso',
        'periodo',
        'turno',
        'status',
    )
    list_display_links = ('tipo', 'requerente',)
    list_filter = ('status',)
    list_per_page = 10


admin.site.register(Requerimento, RequerimentoAdmin)
