'''
URLify  - Write a method to replace all the spaces in a string with %20 . You may
assume that the string has sufficient space at the end to hold the additional characters 
and that you are given the "true" length of the string. If implementing in Java use a 
character array to perform the operation in-place

Example:
Input - "Mr John Smith   ", 13
Output - "Mr%20John%20Smith"

Assumptions:
- only white space or characters and not other chars?
- Ascii only 
- python strings are immutable 
'''

import logging
import pytest
import urllib

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def urlify(str):
    return urllib.parse.quote(str)


@pytest.mark.parametrize('string_1, expected, length',[
    ('cod ing  ','cod%20ing', 9),
    ('', '', 0),
    (' moo     ', '%20moo%20', 9),
    ('  ', '%20%20', 6)
])
def test_strings(string_1, expected, length):
    assert urlify(string_1) == expected