import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_doctor_only_view_access_granted():
    client = APIClient()
    user = User.objects.create_user(
        username='doctor',
        password='password123',
        is_doctor=True
    )
    client.force_authenticate(user=user)
    url = reverse('patients')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_doctor_only_view_access_denied():
    client = APIClient()
    user = User.objects.create_user(
        username='patient',
        password='password123',
        is_doctor=False
    )
    client.force_authenticate(user=user)
    url = reverse('patients')
    response = client.get(url)
    assert response.status_code == 403
