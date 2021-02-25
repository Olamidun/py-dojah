import os
import requests
from dotenv import load_dotenv
from endpoints import Endpoints

load_dotenv()

class PyDojah:

    def __init__(self, app_id, secret_key, sandbox=False):
        self.app_id = app_id
        self.secret_key = secret_key
        self.sandbox = sandbox
        self.endpoint = Endpoints(sandbox=self.sandbox)


    '''Private Methods'''
    # Private method to create headers dictionary
    def _authentication_headers(self):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}
        return headers

    # Private method to send a POST request     
    def _post_data(self, url, data):
        headers = self._authentication_headers()
        response = requests.post(url, headers=headers, data=data)
        return response.json() 

    # Private method to send a GET request
    def _get_data(self, url, params=None):
        headers = self._authentication_headers()

        response = requests.get(url, headers=headers, params=params)
        return response.json()


    '''Dojah Wallet Function'''
    # Endpoint to get Dojah wallet balance
    def get_balance(self):
        return self._get_data(self.endpoint.wallet_balance_endpoint())

    
    '''Crypto Functions'''
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

    # Endpoint for crypto transaction details(Yet to be tested)
    def crypto_transaction_detail(self, transaction_id):
        payload = {
            "transaction_id": transaction_id
        }
        return self._get_data(self.endpoint.get_crypto_wallet_endpoint(), params=payload)

    
    # Endpoint for sending Crypto to another Address(Yet to be tested)
    def send_crypto(self, sender_wallet_id, amount, recipient_address):
        data = {
            "sender_wallet_id": sender_wallet_id,
            "amount": amount,
            "recipient_address": recipient_address
        }
        return self._post_data(self.endpoint.crypto_wallet_endpoint(), data)

    
    '''Data and Airtime functions'''
    # Endpoint to buy Airtime
    def airtime(self, amount, destination):        
        data = {
            "amount": amount,
            "destination": destination
        }
        return self._post_data(self.endpoint.airtime_endpoint(), data)

    # Endpoint to buy data
    def data(self, plan, destination):

        data = {
            "plan": plan,
            "destination": destination
        }

        return self._post_data(self.endpoint.airtime_endpoint(), data)

    # Endpoint to fetch all data plans available
    def data_plan(self):
        return self._get_data(self.endpoint.data_plans_endpoint())



    
        

app_id = os.getenv('APP_ID')
secret_key = os.getenv('TEST_SECRET_KEY')
wallet_id = os.getenv('TEST_WALLET_ADDRESS')

dojah = PyDojah(app_id, secret_key, sandbox=True)
result = dojah.data_plan() 
print(result)
