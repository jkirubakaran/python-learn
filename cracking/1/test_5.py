'''
1.5 One Away : There are three types of edits that can be performed on strings: insert a 
character, remove a character, or replace a character. Given two strings, write a function to
check if they are one (or zero) edits away.
Example
pale, ple --> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Assumptions:
- empty strings returns True 
- ascii characters only
- no white space
- not taking into account other characters like tab, newline,etc
'''

import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def is_one_away(string_1, string_2):
    pass
               


@pytest.mark.parametrize('string_1, string_2, expected',[
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('', '',  True),
    ('pale', 'bake', True)
])
def test_strings(string_1, string_2, expected):
    assert is_one_away(string_1, string_2) == expected