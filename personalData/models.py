from django.db import models
from users.models import CustomUser


class PersonalData(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    birthDate = models.DateField()
    gender = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    cep = models.CharField(max_length=15)
    addressNumber = models.CharField(max_length=15)
    addressComplement = models.CharField(max_length=55, null=True, blank=True)
    addressStreet = models.CharField(max_length=55)
    addressCity = models.CharField(max_length=55)
    addressDistrict = models.CharField(max_length=55)
    addressFederalState = models.CharField(max_length=55)
    healthEnsurance = models.BooleanField()
    healthEnsuranceCompany = models.CharField(max_length=15)
    healthEnsuranceDescription = models.CharField(max_length=15)
    hasHealthData = models.BooleanField()
    hasPersonalData = models.BooleanField(default=True)
    hasPrescription = models.BooleanField()
    hasQrMedication = models.BooleanField()
    schooling = models.CharField(max_length=55)
    civilStatus = models.CharField(max_length=55)
    birthPlace = models.CharField(max_length=55)
    occupation = models.CharField(max_length=55)
    ethnicity = models.CharField(max_length=55)
    familyIncome = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=15, unique=True)
    personalData = models.ForeignKey(to=PersonalData, on_delete=models.CASCADE)

    def __str__(self):
        return self.number



