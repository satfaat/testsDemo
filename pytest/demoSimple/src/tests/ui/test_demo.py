import sys
# sys.path.append("C:\\Users\\user\\Documents\\own\\codeDemo\\pythonDemo\\pytestDemoSimple")

from dotenv import load_dotenv
import pytest
from pytestDemoSimple.src.main.demo import is_even

load_dotenv()


@pytest.mark.skip(reason='This test is no longer needed')
def test_skip_example(even_number) -> None:
    assert is_even(even_number)


@pytest.mark.xfail(reason='An even number plus 1 will never be even')
def test_xfail_example(even_number) -> None:
    assert is_even(even_number + 1)


@pytest.mark.parametrize('even', [2, 4, 6, 8])
@pytest.mark.parametrize('not_even', [3, 5, 7, 9])
def test_valid_even(even, not_even) -> None:
    assert is_even(even)
    assert not is_even(not_even)


@pytest.mark.parametrize('even, not_even', [(2, 3), (4, 5), (6, 7)])
def test_parametrize_example2(even, not_even) -> None:
    assert is_even(even)
    assert not is_even(not_even)


@pytest.mark.parametrize('even, not_even', [(2, 3), pytest.param(5, 5, marks=pytest.mark.xfail)])
def test_parametrize_example3(even, not_even) -> None:
    assert is_even(even)
    assert not is_even(not_even)
