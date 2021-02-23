import requests

class PyDojah:

    def __init__(self, app_id, secret_key, sandbox=True):
        self.app_id = app_id
        self.secret_key = secret_key

        self.base_endpoint = 'https://sandbox.dojah.io'

        if not sandbox:
            self.base_endpoint = 'https://api.dojah.io'


    def get_balance(self):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}

        endpoint = f"{self.base_endpoint}/api/v1/balance"

        # data = {'amount': amount, "destination": destination}

        response = requests.get(endpoint, headers=headers)
        return response.json()


    def create_crypto_wallet(self, wallet_type):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}

        endpoint = f"{self.base_endpoint}/api/v1/wallet/create"

        data = {'wallet_type': wallet_type}

        response = requests.post(endpoint, headers=headers, data=data)
        return response.json()
        


dojah = PyDojah('5fc144c4318b66003e7644c2', 'test_sk_4NJutv5R4FpQFiyC0SPAPcezX', sandbox=True)

result = dojah.create_crypto_wallet('BTC')
print(result)
