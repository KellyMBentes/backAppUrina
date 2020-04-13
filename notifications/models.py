from djongo import models
from users.models import CustomUser
# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=55)

class Option(models.Model):
    item = models.ArrayField(model_container=Item, null=True, blank=True)

class Notification(models.Model):
    option = models.ArrayField(
        model_container=Option, null=True, blank=True
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'
