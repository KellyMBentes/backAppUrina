from django.db import models


class Medicine(models.Model):
    nome = models.CharField(max_length=55, null=True, blank=True)
