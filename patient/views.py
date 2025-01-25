from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer, CustomTokenObtainPairSerializer
from .permissions import IsDoctorPermission
from rest_framework_simplejwt.views import TokenObtainPairView


# ендпоинт списка пациентов
class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctorPermission]



# ендпоинт получения токена
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
