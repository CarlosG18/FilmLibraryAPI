from rest_framework import viewsets
from .serializers import FilmeSerializer, CartegoriaSerializer
from rest_framework.response import Response
from .models import Filme, Categoria

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CartegoriaSerializer

