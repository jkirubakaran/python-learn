from behave import *
from unittest import TestCase
import storage_test as StorageClient
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

@given('we have a valid subscription')
def step_impl(context):
    s = StorageClient._get_subscription('2d74a605-debc-42ee-96d6-588bd3c03c9a')
    if s.display_name is None:
        assert(s.display_name is not None)

@when('we configure a Storage Account')
def step_impl(context):
    # assert (context.config.userdata['foo'] == 'bar'), "Invalid subscription"
    pass

@then('the Storage Account should have encryption enabled')
def step_impl(context):
    pass

@then(u'the Storage Account should have https enabled')
def step_impl(context):
    pass

@then(u'the Storage Account should have logging enabled')
def step_impl(context):
    pass