from djongo import models
from users.models import CustomUser


class Beverage(models.Model):
    name = models.CharField(max_length=55, null=True, blank=True)


class LiquidIntake(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createdDate = models.DateField(auto_now_add=True)
    beverage = models.ArrayField(model_container=Beverage, null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)