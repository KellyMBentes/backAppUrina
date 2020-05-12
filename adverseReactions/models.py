from django.db import models
from users.models import CustomUser
from medicines.models import Medicine


class AdverseReaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    skin_rash = models.BooleanField(default=False)
    skin_swelling = models.BooleanField(default=False)
    blood_pressure_fall = models.BooleanField(default=False)
    consciousness_loss = models.BooleanField(default=False)
    difficult_of_breathing = models.BooleanField(default=False)
    comment = models.CharField(max_length=240)
