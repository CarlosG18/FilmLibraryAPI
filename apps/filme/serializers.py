from rest_framework import serializers
from .models import Filme, Categoria
from .validators import validate_data

class FilmeSerializer(serializers.ModelSerializer):
    categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())

    class Meta:
        model = Filme
        fields = ['nome','ano_de_estreia','poster','categorias']

    def validate(self, dados):
        
        if validate_data(dados['ano_de_estreia']):
            raise serializers.ValidationError('Valor para a data inválido!')

        return dados 

class CartegoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'