from djongo import models
from users.models import CustomUser


# Objeto notification possui referencia a todas as opcoes do usuario
class Notification(models.Model):
    userId = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    isSelectedAll = models.BooleanField(default=True)  # Marca todas as opçoes do usuario como True
    isPriority = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class Option(models.Model):
    notificationId = models.ForeignKey(Notification, on_delete=models.CASCADE)
    isSelected = models.BooleanField(default=True)
    isPriority = models.BooleanField(default=False)
    text = models.CharField(max_length=100)
    type = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
