from django.db import models

class Estudante(models.Model):
    nome_completo = models.CharField(max_length=120)
    endereco_residencial = models.CharField(max_length=250)
    cidade_moradia = models.CharField(max_length=100)
    email_pessoal = models.EmailField()
    nome_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo
