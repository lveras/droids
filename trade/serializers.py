from rest_framework import serializers
from .models import Demanda
from django.contrib.auth.models import User


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id', 'status', 'descricao', 'estado', 'cidade', 'cep',
                  'endereco', 'num_endereco', 'comp_endereco']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
