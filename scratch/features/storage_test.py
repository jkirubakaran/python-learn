
from azure.mgmt.storage import StorageManagementClient
from azure.common.client_factory import get_client_from_auth_file


storage_client = get_client_from_auth_file(StorageManagementClient)

for item in storage_client.storage_accounts.list():
    foo = vars(item)
    encrypt_obj = foo['encryption']
    print(encrypt_obj.services.file.enabled)