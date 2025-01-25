import pytest
from django.contrib.auth import get_user_model
from patient.models import Patient, Diagnose

User = get_user_model()


# проверка на создание пользователя (доктор)
@pytest.mark.django_db
def test_create_doctor_user():
    user = User.objects.create_user(
        username='steve',
        password='password123',
        is_doctor=True
    )
    assert user.username == 'steve'
    assert user.is_doctor is True


# проверка на создание пользователя (не доктор)
@pytest.mark.django_db
def test_create_non_doctor_user():
    user = User.objects.create_user(
        username='arnold',
        password='password123',
        is_doctor=False
    )
    assert user.username == 'arnold'
    assert user.is_doctor is False


# проверка на создание пациента
@pytest.mark.django_db
def test_create_patient():
    from datetime import date
    patient = Patient.objects.create(
        date_of_birth=date(year=1980, month=3, day=18),
    )
    assert patient.date_of_birth == date(year=1980, month=3, day=18)


# проверка на создание диагноза
@pytest.mark.django_db
def test_create_diagnose():
    from datetime import date
    patient = Patient.objects.create(
        date_of_birth=date(year=1980, month=3, day=18),
    )
    diagnose = Diagnose.objects.create(
        name="Headache",
        description="головная боль",
        patient=patient

    )
    assert diagnose.name == "Headache"
    assert diagnose.description == "головная боль"
    assert diagnose.patient == patient
