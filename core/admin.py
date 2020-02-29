from django.contrib import admin
from .models import Veiculo, Pessoa, Marca, Parametros, MovRotativo, Mensalista

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo','valor_hora','checkin', 'checkout', 'horas_total','total','pago')

admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)


# Register your models here.
