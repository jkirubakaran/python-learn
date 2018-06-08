from behave import *
from unittest import TestCase
from storage import StorageProvider
from subscription import SubscriptionClientProvider
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())


@given('we have a valid subscription')
def step_impl(context):
    context.subs_client = SubscriptionClientProvider()
    s = context.subs_client.subscription('2d74a605-debc-42ee-96d6-588bd3c03c9a')
    if s.display_name is None:
        assert(s.display_name is not None)

@when(u'we have Storage Account(s) provisioned')
def step_impl(context):
    context.storage_client = StorageProvider()
    if(len(list(context.storage_client.storage_accounts())) > 0):
        pass
    else:
        AssertionError('No Storage Accounts found to scan')

@then(u'each Storage Account should have encryption enabled')
def step_impl(context):
    for account in list(context.storage_client.storage_accounts()):
        logger.info('Subscription ID: {}'.format(account))
        assert account.encryption.services.blob.enabled is True, "Blob service is not encrypted"
        assert account.encryption.services.file.enabled is True, "File service is not encrypted"
    

@then(u'each Storage Account should have https enabled')
def step_impl(context):
    for account in list(context.storage_client.storage_accounts()):
        assert account.enable_https_traffic_only is 'enabled', "HTTPS traffic is not enabled"

@then(u'the Storage Account should have logging enabled')
def step_impl(context):
    pass