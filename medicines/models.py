from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=55, default='Not specified')

    def __str__(self):
        return self.name
