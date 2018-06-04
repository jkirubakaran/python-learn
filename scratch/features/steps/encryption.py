from behave import *
from unittest import TestCase

@given('we have a "{type}" subscription')
def step_impl(context, type):
    pass

@when('we configure a Storage Account')
def step_impl(context):
    assert (context.config.userdata['foo'] == 'bar'), "Invalid subscription"

@then('the Storage Account should have encryption enabled')
def step_impl(context):
    pass

@then(u'the Storage Account should have https enabled')
def step_impl(context):
    pass

@then(u'the Storage Account should have logging enabled')
def step_impl(context):
    pass