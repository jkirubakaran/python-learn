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
    str =  str.replace(" ", "")
    if str == '':
        return True
    
    sorted_list = sorted(str.lower())
    logger.info('list sorted , remove white space and lower cased: {}'.format(sorted_list))
    for i in range(0, len(sorted_list), 2):
        logger.info('i={} i+1={}'.format(sorted_list[i], sorted_list[i+1]))
        if sorted_list[i] != sorted_list[i+1]:
            logger.info('meow')
            return False
        elif len(str) % 2 != 0 and i + 1 == len(sorted_list): #odd size string and at last character
            return True
    
    return True
               


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