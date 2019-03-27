from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    mensagem = models.TextField()
    receber_noticias = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

    