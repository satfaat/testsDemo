import os
import logging
from dotenv import load_dotenv

load_dotenv()
LOGGER: logging.Logger = logging.getLogger(__name__)


def test_dotenv() -> None:
    LOGGER.info('logs output: ' + os.environ["ADMIN_EMAIL"])
    assert 'admin@example.org' == os.environ["ADMIN_EMAIL"]


def test_uppercase() -> None:
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed() -> None:
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes() -> None:
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
