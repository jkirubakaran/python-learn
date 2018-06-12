'''
1.2 Check Permutation - Given two strings , write a method to decide if one is 
a permutation of the other 

Assumptions :
- empty string is not a permutation of another string
- two empty strings are not permutations 
- case insensitive comparison of strings 
'''

import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def checkStrings(str1, str2):
    pass


@pytest.mark.parametrize('test_input, expected', [
    ('coding', True),
    ('fire', True),
    ('network', True),
    ('Baby', False),
    ('moo', False),
    ('', True)
])
def test_strings(string_1, string_2, expected):
    assert is_unique_same_data_structure(test_input) is expected