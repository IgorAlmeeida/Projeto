from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    men = {'mensagem': 'Igor Aqui'}
    return render(request,"core/index.html",men)