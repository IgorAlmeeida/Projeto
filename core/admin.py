from django.contrib import admin
from .models import Veiculo, Pessoa, Marca, Parametros, MovRotativo, Mensalista, MovMensalista

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo','valor_hora','checkin', 'checkout', 'horas_total','total','pago')

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista','data_pagamento', 'total')


admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)


# Register your models here.
