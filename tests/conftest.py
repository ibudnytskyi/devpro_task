import pytest
from generator.generator import generate_sample_data


@pytest.fixture
def data():
    return generate_sample_data()
