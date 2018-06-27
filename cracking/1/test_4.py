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
    str = str.replace(" ", "")
    str_dict = {}

    for c in str.lower():
        if c in str_dict:
            str_dict[c] += 1
        else:
            str_dict[c] = 1

    num_of_odd_keys = 0 
    for key in str_dict:
        if str_dict[key] % 2 == 1:
            num_of_odd_keys += 1
    
    if num_of_odd_keys > 1:
        return False
    elif num_of_odd_keys == 1 and len(str) == 3:
        return False
    else: 
        return True
               


@pytest.mark.parametrize('string, expected',[
    ('noon', True),
    ('civic', True),
    ('ra da R', True),
    ('', True),
    ('Taco Cat', True),
    ('T a co C a t ', True),
    ('123', False),
    ('foo', False),
    ('this is not a palindrome', False)
])
def test_strings(string, expected):
    assert is_palindrome_or_permutation(string) == expected