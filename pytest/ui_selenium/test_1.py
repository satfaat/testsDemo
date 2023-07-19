import pytest


def test_firefox(selenium):
    selenium.get('http://www.example.com')
    assert 'Example' in selenium.title
    selenium.quit()
