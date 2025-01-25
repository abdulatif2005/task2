import pytest
from rest_framework.test import APIRequestFactory
from patient.permissions import IsDoctorPermission
from django.contrib.auth import get_user_model

User = get_user_model()


# проверка на доступ если пользователь доктор
@pytest.mark.django_db
def test_is_doctor_permission_granted():
    factory = APIRequestFactory()
    user = User.objects.create_user(
        username='doctor',
        password='password123',
        is_doctor=True
    )
    request = factory.get('/some-url/')
    request.user = user
    permission = IsDoctorPermission()
    assert permission.has_permission(request, None) is True


# проверка на доступ если пользователь доктор
@pytest.mark.django_db
def test_is_doctor_permission_denied():
    factory = APIRequestFactory()
    user = User.objects.create_user(
        username='notdoctor',
        password='password123',
        is_doctor=False
    )
    request = factory.get('/some-url/')
    request.user = user
    permission = IsDoctorPermission()
    assert permission.has_permission(request, None) is False
