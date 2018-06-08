from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.subscription import SubscriptionClient
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

class SubscriptionClientProvider:

    _subs_client = get_client_from_cli_profile(SubscriptionClient)

    @classmethod
    def subscription(cls, subscription_id):
        try:
            return cls._subs_client.subscriptions.get(subscription_id)
            
        except Exception as e:
            logger.error(e, 'could not get subscription, danger will robinson!')
            raise e



if __name__ == '__main__':
    s = SubscriptionClientProvider()