from rest_framework import serializers
from .models import Filme, Categoria

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class CartegoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'