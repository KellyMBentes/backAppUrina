from djongo import models
from users.models import CustomUser



class LiquidIntake(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    beverage = models.CharField(max_length=55, null=True, blank=True)
    createdDate = models.DateField(auto_now_add=True)
    volume = models.FloatField(null=True, blank=True)
