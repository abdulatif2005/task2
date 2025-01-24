from rest_framework import serializers
from .models import Patient, Diagnose


class PatientSerializer(serializers.ModelSerializer):
    diagnoses = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Patient
        fields = ["id", "date_of_birth", "diagnoses", "created_at"]
