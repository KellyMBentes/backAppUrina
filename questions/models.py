from djongo import models
from users.models import CustomUser


class QuestionForm(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=55, null=True, blank=True)
    slider = models.BooleanField(default=False)
    type = models.CharField(max_length=55, null=True, blank=True)


class Option(models.Model):
    formId = models.ForeignKey(QuestionForm, on_delete=models.CASCADE)
    text = models.CharField(max_length=55, null=True, blank=True)
