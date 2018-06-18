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

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def urlify(str, length):
    while(str.find(' ') != -1):
        index = str.find(' ')
        str = str[:index] + '%20' + str[index + 1: -2 ]
        logger.info('str is {}'.format(str))

    return str 

def urlify_2(str, length):
    str = list(str)
    while(str.index(' ') != -1):
       index = str.index(' ')
       str[index] = '%'
       str.insert(index + 1, '2')
       str.insert(index + 2, '0')
       str.pop()
       str.pop()
        
    return ''.join(str)

@pytest.mark.parametrize('string_1, expected, length',[
    ('cod ing  ','cod%20ing', 9),
    ('', '', 0),
    (' moo     ', '%20moo%20', 9),
    ('      ', '%20%20', 6)
])
def test_strings(string_1, expected, length):
    assert urlify_2(string_1, length) == expected
