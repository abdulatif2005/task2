from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer, CustomTokenObtainPairSerializer
from .permissions import IsDoctorPermission
from rest_framework_simplejwt.views import TokenObtainPairView

class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctorPermission]



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
