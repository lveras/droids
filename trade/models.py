from django.db import models
from django.contrib.auth.models import User
# from localflavor.br.forms import BRZipCodeField

STATUS = (
    (1, "Aberta"),
    (2, "Finalizada"),
)


class Anunciante(models.Model):

    class Meta:
        db_table = 'anunciante'

    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    nome = models.CharField(max_length=256)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome


class Demanda(models.Model):

    class Meta:
        db_table = 'demanda'

    status = models.IntegerField(choices=STATUS, default=1)
    descricao = models.CharField(max_length=256)
    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=256)
    cidade = models.CharField(max_length=256)
    cep = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    num_endereco = models.IntegerField()
    comp_endereco = models.CharField(max_length=256)

    def __str__(self):
        return self.descricao
