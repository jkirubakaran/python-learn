'''
1.1 Is Unique - Implement a algorithm to determine if a string has all unique 
characters. What if you cant use any additional data structures ?

Assumptions :
- empty string should be True
- data structure above is a array of characters , so a list in python
- case insensitive 
'''

import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def is_unique(str):
    
    char_set = set()

    logger.info('input string: {}'.format(str))
    for char in str.lower():
        if char in char_set:
            logger.info('looking up {} in set found a match'.format(char))
            return False
        else:
            char_set.add(char)
        
    logger.info('Finished searching string')
    return True

def is_unique_same_data_structure(str):
    
    for i in range(len(str)):
        for char in str[i:]:
            if char is str[i]:
                logger.info('found a match for {}'.format(char))
                return False
            
    
    logger.info('Finished searching string')
    return True


@pytest.mark.parametrize('test_input, expected', [
    ('coding', True),
    ('fire', True),
    ('network', True),
    ('Baby', False),
    ('moo', False),
    ('', True)
])
def test_strings(test_input, expected):
    assert is_unique_same_data_structure(test_input) is expected

is_unique_same_data_structure('moo')

