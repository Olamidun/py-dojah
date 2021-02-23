import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PyDojah:

    def __init__(self, app_id, secret_key, sandbox=True):
        self.app_id = app_id
        self.secret_key = secret_key

        self.base_endpoint = 'https://sandbox.dojah.io'

        if not sandbox:
            self.base_endpoint = 'https://api.dojah.io'


    def _authentication_headers(self):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}

        return headers


    def get_balance(self):
        headers = self._authentication_headers()

        endpoint = f"{self.base_endpoint}/api/v1/balance"


        response = requests.get(endpoint, headers=headers)
        return response.json()

    
    def crypto_wallet_details(self, wallet_id):
        headers = self._authentication_headers()

        endpoint = f"{self.base_endpoint}/api/v1/wallet?wallet_id={wallet_id}"
        print(endpoint)

        response = requests.get(endpoint, headers=headers)
        return response.json()

        


    def create_crypto_wallet(self, wallet_type):
        headers = self._authentication_headers()

        endpoint = f"{self.base_endpoint}/api/v1/wallet/create"

        data = {'wallet_type': wallet_type}

        response = requests.post(endpoint, headers=headers, data=data)
        return response.json()
        

app_id = os.getenv('APP_ID')
secret_key = os.getenv('TEST_SECRET_KEY')

dojah = PyDojah(app_id, secret_key, sandbox=True)

result = dojah.crypto_wallet_details('26e5233e-90b5-446d-9a77-aff73ccb7f81') 
print(result)





# def _get(self, endpoint_extension):
#         self.endpoint = f"{self.base_endpoint}{endpoint_extension}"
#         headers = {'Authorization': self.secret_key, 'AppId': self.app_id}
#         response = requests.get(self.endpoint, headers=headers)
#         return response.json()