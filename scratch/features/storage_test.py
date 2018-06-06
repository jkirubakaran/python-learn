from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.subscription import SubscriptionClient
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

storage_client = get_client_from_cli_profile(StorageManagementClient)

subs_client = get_client_from_cli_profile(SubscriptionClient)

@classmethod
def _get_subscription(subscription_id):
    try:
        return subs_client.subscriptions.get(subscription_id)
        
    except Exception as e:
        logger.error(e)
        raise Exception('could not get subscription, danger will robinson!')

@classmethod
def storage_accounts():
    storage_list = storage_client.storage_accounts.list
    

#sub = _get_subscription(subscription_id='2d74a605-debc-42ee-96d6-588bd3c03c9a')

# logger.info('dsub' in sub.display_name)