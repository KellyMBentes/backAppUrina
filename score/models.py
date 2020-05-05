from django.db import models
from users.models import CustomUser


class Score(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.IntegerField(default=1, blank=True, null=True)
    exp = models.IntegerField(default=10, blank=True, null=True)
    consecutiveDays = models.IntegerField(default=0, blank=True, null=True)
