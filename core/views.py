from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa  

from .forms import PessoaForm

# Create your views here.

def home (request):
    men = {'mensagem': 'Igor Aqui'}
    return render(request,"core/index.html",men)

def lista_pessoas(request):
    #LISTANDO AS PESSOAS
    pessoas = Pessoa.objects.all()

    #CRIANDO O FORM DE PESSOA
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}

    return render(request, "core/clientes.html", data)

#FUNCAO QUE CRIA A PESSOA
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)

    #SALVANDO NO BANCO DE DADOS
    if(form.is_valid()):
        form.save()

    return redirect('lista_pessoas')

def pessoa_update(request, id):
    data ={}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form 

    if request.method == 'POST':
        if (form.is_valid()):
            form.save()
            return redirect('lista_pessoas')
    else:
        return render(request, 'core/clientes_update.html', data)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if (request.method == "POST"):
        pessoa.delete()
        return redirect("lista_pessoas")
    else:
        return render(request, "core/delete_pessoa.html", {'pessoa': pessoa})