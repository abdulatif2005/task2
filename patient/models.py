from django.contrib.auth.models import AbstractUser
from django.db import models


#модель пользователя
class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)


#модель пациентов
class Patient(models.Model):
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


#модель диагнозов
class Diagnose(models.Model):
    name = models.CharField(max_length=125, )
    description = models.TextField()
    patient = models.ForeignKey(Patient, related_name="diagnoses", on_delete=models.CASCADE)
