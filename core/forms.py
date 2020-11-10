from django.forms import ModelForm
from .models import Pessoa

#CLASSE QUE DEFINE O FORMULÁRIO
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'