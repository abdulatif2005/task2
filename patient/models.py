from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField


class Patient(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    date_of_birth = models.DateField()


class Diagnose(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=125, )
    description = models.TextField()
    patient = models.ForeignKey(Patient, related_name="diagnoses")
