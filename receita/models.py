from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):

    categoria = models.TextField(primary_key=True)
    
class Receita(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	ingredientes = models.TextField(blank=True, null=True)
	modo_preparo = models.TextField(blank=True, null=True)
	tempo_preparo = models.TimeField(null=True, blank=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	data_criacao = models.DateTimeField(null=True, blank=True)
	publico_privado = models.BooleanField(default=False)

class Avaliacao(models.Model):
    
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(blank=True, null=True)
    comentarios = models.TextField(max_length=255, blank=False)
    

		