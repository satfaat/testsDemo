import requests
from unittest.mock import Mock, patch


def most_common_word_in_web_page(words, url):
    """
    finds the most common word from a list of words
    in a web page, identified by its URL
    """
    response = requests.get(url)
    return most_common_word(words, response.text)

def most_common_word(words, text):
    """
    finds the most common word from a list of words
    in a piece of text
    """
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

def test_with_patch():
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    with patch('webcount.functions.requests', mock_requests):
        result = most_common_word_in_web_page(
            ['a', 'b', 'c'],
            'https://python.org/',
        )
    assert result == 'b', \
        'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] \
            == 'https://python.org/', 'called with right URL'