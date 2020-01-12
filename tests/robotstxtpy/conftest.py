import pytest


@pytest.fixture
def example_valid_url():
    return 'https://www.example.com/'


@pytest.fixture
def example_invalid_url():
    return '.example.com/'
