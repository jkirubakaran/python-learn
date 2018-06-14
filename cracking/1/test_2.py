'''
1.2 Check Permutation - Given two strings , write a method to decide if one is 
a permutation of the other 

Assumptions :
- two empty strings are not permutations 
- case insensitive comparison of strings 
- whitespace does count as a valid character
- non string input not allowed  

missed:
- once sorted maybe do a MD5 and compare ?
- just do a simple == check instead of checking all characters with a loop
'''

import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def _is_empty_strings(str1, str2):
    return str1 == '' or str2 == ''

def _is_not_same_length(str1, str2):
    return len(str1) != len(str2)

def _input_not_strings(str1, str2):
    return type(str1).__name__ != 'str' or type(str2).__name__ != 'str'

def check_if_permutations(str1, str2):

    if ( _input_not_strings(str1, str2) or
         _is_empty_strings(str1, str2) or
         _is_not_same_length(str1, str2)
    ):
        return False
    
    return sorted(list(str1.lower())) == sorted(list(str2.lower()))
    


@pytest.mark.parametrize('string_1, string_2, expected', [
    ('coding','ingcod', True),
    ('fire','erif', True),
    ('network', 'work', False),
    ('Baby', 'bbay', True),
    ('moo', 'm', False),
    ('', '', False),
    (None, 'moo', False)
])
def test_strings(string_1, string_2, expected):
    assert check_if_permutations(string_1, string_2) is expected

