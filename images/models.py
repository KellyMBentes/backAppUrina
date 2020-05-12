from djongo import models
from users.models import CustomUser


class Image(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    firebaseKey = models.CharField(max_length=55)
