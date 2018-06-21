'''
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation
of a palindrome. A palindrome is a word or phrase that is the same forward and backwards. 
A permutation is a rearrangement of letters. The palindrome does not need to be restricted to 
just dictionary words.

Example
Input : Tact Coa
Output: True(permutations: 'taco cat', 'atco cta', etc.)

Assumptions:
- empty string returns True 
- ascii characters only
- not testing for weird characters like i'm 
- case insensitive
- white space does not matter 
- not taking into account other characters like tab, newline,etc
'''

import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def is_palindrome_or_permutation(str):
    if str == '':
        return True
    
    str =  str.replace(" ", "")
    sorted_list = sorted(str.lower())

    for index, value in enumerate(sorted_list):
        if index == len(sorted_list) - 1:
            return True 
        elif index != 0:
            if (sorted_list[index - 1] == value):
                pass
            else:
                return False
               


@pytest.mark.parametrize('string, expected',[
    ('noon', True),
    ('civic', True),
    ('ra da R', True),
    ('', True),
    ('Taco Cat', True),
    ('123', False),
    ('foo', False),
    ('this is not a palindrome', False)
])
def test_strings(string, expected):
    assert is_palindrome_or_permutation(string) == expected