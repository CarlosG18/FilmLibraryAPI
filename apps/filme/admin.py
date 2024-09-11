from django.contrib import admin
from .models import Filme, Categoria

# Register your models here.
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['nome','ano']
    list_filter = ['categoria',]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome',]
