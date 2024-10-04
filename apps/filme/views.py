from rest_framework import viewsets, status
from .serializers import FilmeSerializer, CartegoriaSerializer
from rest_framework.response import Response
from .models import Filme, Categoria
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "error": "username e password são nescessários!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username, password=password).exists():
            return Response({
                "error": "usuario já cadastrado!"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(username=username, password=password)
            return Response({
                "message": "usúario cadastrado com sucesso!"
            }, status=status.HTTP_201_CREATED)

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    authentication_classes = [TokenAuthentication]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CartegoriaSerializer
    permission_classes = [AllowAny]
