import pytest
from app.schemas import UserCreate


def test_user_create_schema():
    user_data = {'email': 'test@example.com'}
    user = UserCreate(**user_data)
    assert user.email == 'test@example.com'


def test_user_create_schema_invalid_email():
    with pytest.raises(ValueError):
        UserCreate(email='invalid-email')