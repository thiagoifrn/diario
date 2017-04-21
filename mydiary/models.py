from django.db import models
from django.utils import timezone

class Diario(models.Model):
    usuario = models.ForeignKey('auth.User')
    tarefa = models.TextField()
    resultados = models.TextField()
    avaliacao = models.TextField()
    atividades_futuras = models.TextField()
    data_entrada = models.DateTimeField('data de entrada', auto_now_add=True)
    data_saida = models.DateTimeField('data de saida')




