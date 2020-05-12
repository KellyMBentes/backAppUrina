from django.db import models


class Medicine(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome
