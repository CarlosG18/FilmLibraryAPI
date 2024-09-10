from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def clean_senha(self):
        """
            função para validação da senha

            - a senha deverá conter:
                - Comprimento mínimo de 8 caracteres.
                - Pelo menos uma letra maiúscula.
                - Pelo menos uma letra minúscula.
                - Pelo menos um dígito.
                - Pelo menos um caractere especial (como @, #, $, etc.).
        """

        senha = self.senha
        senha_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if senha:
            if re.match(senha_regex, senha):
                return senha
            else:
                raise ValidationError("formato de senha invalido!")

    def __str__(self) -> str:
        return self.nome