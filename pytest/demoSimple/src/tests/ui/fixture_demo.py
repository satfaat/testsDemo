import pytest


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture) -> None:
    assert example_fixture == 1
