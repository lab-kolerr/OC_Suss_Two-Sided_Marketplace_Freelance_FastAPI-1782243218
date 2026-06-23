import pytest
from app.utils import some_utility_function


def test_some_utility_function():
    result = some_utility_function('input')
    assert result == 'expected_output'