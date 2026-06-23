import pytest
from app.models import User


def test_user_creation():
    user = User(email='test@example.com', hashed_password='hashed_password')
    assert user.email == 'test@example.com'
    assert user.hashed_password == 'hashed_password'


def test_user_email_uniqueness():
    user1 = User(email='unique@example.com', hashed_password='password1')
    user2 = User(email='unique@example.com', hashed_password='password2')
    assert user1.email == user2.email