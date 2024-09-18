from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='categorias/')

    def __str__(self) -> str:
        return self.nome
    
class Filme(models.Model):
    nome = models.CharField(max_length=200)
    ano_de_estreia = models.DateField()
    categorias = models.ManyToManyField(Categoria, blank=True)
    poster = models.ImageField(upload_to='filmes/')

    def __str__(self) -> str:
        return self.nome

