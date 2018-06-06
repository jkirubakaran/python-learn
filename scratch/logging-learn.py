import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('test.log')


def add(y, x):
    return x + y

def subtract(x, y):
    return x - y

num_1 = 10
num_2 = 5
 
add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
sub_result = subtract(num_1, num_2)
logger.info('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))

