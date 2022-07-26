from django.db import models

# Create your models here.

class Contato(models.Model):
    ESTIPULANTE = models.CharField(primary_key=True, max_length=20)
    CELULAR = models.CharField(max_length=20)
    DT_CONTRATO = models.CharField(max_length=20)
    SITUACAO = models.CharField(max_length=20)
