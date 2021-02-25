import os
import requests
from dotenv import load_dotenv
from endpoints import Endpoints

load_dotenv()

class PyDojah:

    def __init__(self, app_id, secret_key):
        self.app_id = app_id
        self.secret_key = secret_key

        self.endpoint = Endpoints()

    # Private method to create headers dictionary
    def _authentication_headers(self):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}

        return headers

    def _post_data(self, url, data):
        headers = self._authentication_headers()
        response = requests.post(url, headers=headers, data=data)
        return response.json() 

    def _get_data(self, url, params=None):
        headers = self._authentication_headers()

        response = requests.get(url, headers=headers, params=params)
        return response.json()


    # Endpoint to get Dojah wallet balance
    def get_balance(self):
        return self._get_data(self.endpoint.wallet_balance_endpoint())

    # Endpoint to get crypto wallet details
    def crypto_wallet_details(self, wallet_id):
        
        payload = {
            "wallet_id": wallet_id
        }
        return self._get_data(self.endpoint.get_crypto_wallet_endpoint(), params=payload)
        
    # Endpoint to create crypto wallet
    def create_crypto_wallet(self, wallet_type):

        data = {"wallet_type": wallet_type}

        return self._post_data(self.endpoint.crypto_wallet_endpoint(), data)
        

    # Endpoint to buy Airtime
    def airtime(self, amount, destination):
        
        data = {
            "amount": amount,
            "destination": destination
        }

        return self._post_data(self.endpoint.airtime_endpoint(), data)

    def data(self, plan, destination):

        data = {
            "plan": plan,
            "destination": destination
        }

        return self._post_data(self.endpoint.airtime_endpoint(), data)
        

app_id = os.getenv('APP_ID')
secret_key = os.getenv('TEST_SECRET_KEY')
wallet_id = os.getenv('TEST_WALLET_ADDRESS')

dojah = PyDojah(app_id, secret_key)
result = dojah.crypto_wallet_details(wallet_id) 
print(result)
