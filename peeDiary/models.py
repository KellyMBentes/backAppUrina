from django.db import models
from users.models import CustomUser


class PeeDiary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    peeVolume = models.FloatField(blank=True, null=True)
    effortToUrinate = models.IntegerField(blank=True, null=True)
    hasLost = models.BooleanField(default=False)
    isDoingPhysicalActivity = models.BooleanField(default=False)
    referenceVolume = models.FloatField(default=200, blank=True, null=True)


