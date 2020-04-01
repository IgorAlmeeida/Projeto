from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

def home (request):
    men = {'mensagem': 'Igor Aqui'}
    return render(request,"core/index.html",men)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, "core/clientes.html", {'pessoa': pessoas})