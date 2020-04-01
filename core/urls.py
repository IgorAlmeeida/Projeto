from django.urls import path, include
from .views import home, lista_pessoas

urlpatterns = [
    path('', home),
    path('clientes', lista_pessoas),
]
