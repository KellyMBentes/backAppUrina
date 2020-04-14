from djongo import models
from users.models import CustomUser


class Option(models.Model):
    text = models.CharField(max_length=55, null=True, blank=True)


class QuestionForm(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    option = models.ArrayField(model_container=Option, null=True, blank=True)
    title = models.CharField(max_length=55, null=True, blank=True)
    slider = models.BooleanField(default=False)
    type = models.CharField(max_length=55, null=True, blank=True)
