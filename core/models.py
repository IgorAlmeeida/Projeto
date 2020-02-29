from django.db import models
import math


# Create your models here.

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    ESTADOS_FEDERADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'))

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICES)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10,default='S/N')
    bairro = models.CharField(max_length=100, default='Centro')
    cidade = models.CharField(max_length=50, default='Catende')
    estado = models.CharField(max_length=2, choices=ESTADOS_FEDERADOS)
    telefone = models.CharField(max_length=20)
    

    def __str__ (self):
        return self.nome

class Marca (models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return self.nome

class Veiculo (models.Model):
    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey('Pessoa', on_delete= models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField(default='', blank=True)

    def __str__(self):
        return self.marca.nome + " - " + self.placa


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "Parametros Gerais"

class MovRotativo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete= models.CASCADE)
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        d1 = self.checkout
        d2 = self.checkin

        if (type(d1) != type(d2)):
            return 0
        else:
            return math.ceil((d1 - d2).total_seconds() / 3600)
    def total(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.placa 


class Mensalista (models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete = models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits= 5, decimal_places = 2)
    
    def __str__(self):
        return str(veiculo) + " - " + str(inicio) 

