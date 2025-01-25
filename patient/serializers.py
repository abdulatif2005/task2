from rest_framework import serializers
from .models import Patient, Diagnose
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Сериализатор при получении данных Пациента
class PatientSerializer(serializers.ModelSerializer):
    diagnoses = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Patient
        fields = ["id", "date_of_birth", "diagnoses", "created_at"]


# Сериализатор для получения токена
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_doctor'] = user.is_doctor
        return token
