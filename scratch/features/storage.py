from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.storage import StorageManagementClient
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

class StorageProvider:

    storage_client = get_client_from_cli_profile(StorageManagementClient)

    def __init__(self):
        pass


    @classmethod
    def storage_accounts(cls):
        try:
            return cls.storage_client.storage_accounts.list()
        except Exception as e:
            logger.error(e)
            raise e
     

if __name__ == '__main__':
    provider = StorageProvider()
    # logger.info(type(provider.storage_accounts()))
    for account in provider.storage_accounts():
        logger.info(account)

#sub = _get_subscription(subscription_id='2d74a605-debc-42ee-96d6-588bd3c03c9a')

# logger.info('dsub' in sub.display_name)