import pytest
from django.contrib.auth import get_user_model
from company.models import Company

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.check_password("testpass")


@pytest.mark.django_db
def test_create_company():
    user1 = User.objects.create_user(username="user1", email="user1@example.com", password="password")
    user2 = User.objects.create_user(username="user2", email="user2@example.com", password="password")
    user3 = User.objects.create_user(username="user3", email="user3@example.com", password="password")

    company = Company.objects.create(
        company_name="Test Company",
        company_address="123 Test St",
        company_email="company@example.com",
        company_phone="123456789",
        user1=user1,
        user2=user2,
        user3=user3
    )

    assert company.company_name == "Test Company"
    assert company.company_email == "company@example.com"
    assert company.user1 == user1
    assert company.user2 == user2
    assert company.user3 == user3


@pytest.mark.django_db
def test_company_str():
    company = Company.objects.create(
        company_name="Sample Corp",
        company_email="sample@example.com"
    )
    assert str(company) == "Sample Corp"


@pytest.mark.django_db
def test_user_str():
    user = User.objects.create_user(username="user123", email="user123@example.com", password="password")
    assert str(user) == "user123@example.com"
