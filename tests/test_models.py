import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_doctor_user():
    user = User.objects.create_user(
        username='steve',
        password='password123',
        is_doctor=True
    )
    assert user.username == 'steve'
    assert user.is_doctor is True


@pytest.mark.django_db
def test_create_non_doctor_user():
    user = User.objects.create_user(
        username='arnold',
        password='password123',
        is_doctor=False
    )
    assert user.username == 'arnold'
    assert user.is_doctor is False
