from django.db import models
from users.models import CustomUser
# Create your models here.

class PersonalData(models.Model):
    user                       = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    name                       = models.CharField(max_length=55)
    birthDate                  = models.DateField()
    gender                     = models.CharField(max_length=55)
    cpf                        = models.CharField(max_length=15)
    rg                         = models.CharField(max_length=15)
    addressNumber              = models.CharField(max_length=15)
    addressComplement          = models.CharField(max_length=55)
    phone                      = models.CharField(max_length=15)
    healthEnsurance            = models.BooleanField()
    healthEnsuranceCompany     = models.CharField(max_length=15)
    healthEnsuranceDescription = models.CharField(max_length=15)
    hasHealthData              = models.BooleanField()
    hasPersonalData            = models.BooleanField()
    hasPrescription            = models.BooleanField()
    hasQrMedicaiton            = models.BooleanField()

    def __str__(self):
        return self.name + self.user.email

