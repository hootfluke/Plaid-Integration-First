from plaid import ApiClient, Configuration
from plaid.api.plaid_api import PlaidApi
from .config import PLAID_CLIENT_ID, PLAID_SECRET, PLAID_ENV


def get_plaid_client(request):
    configuration = Configuration(
        host=PLAID_ENV,
        api_key={
            "clientId": PLAID_CLIENT_ID,
            "secret": PLAID_SECRET,
        },
    )
    api_client = ApiClient(configuration)
    client = PlaidApi(api_client)


    return configuration(
        client_id=PLAID_CLIENT_ID,
        secret=PLAID_SECRET,
        environment=PLAID_ENV
    )