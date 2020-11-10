from django.urls import path, include
from .views import home, lista_pessoas, pessoa_novo, pessoa_update, pessoa_delete

urlpatterns = [
    path('', home),
    path('clientes', lista_pessoas, name="lista_pessoas"),
    path('clientes/new', pessoa_novo, name="pessoa_novo"),
    path('clientes/update/<id>/', pessoa_update, name="pessoa_update"),
    path('clientes/delete/<id>/', pessoa_delete, name="pessoa_delete")
]
