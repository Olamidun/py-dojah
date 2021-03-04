import os
import requests
from dotenv import load_dotenv
from endpoints import EndPoints

load_dotenv()

class PyDojah:

    def __init__(self, app_id, secret_key, sandbox=False):
        self.app_id = app_id
        self.secret_key = secret_key
        self.sandbox = sandbox
        self.endpoint = EndPoints(sandbox=self.sandbox)


    '''Private Methods'''
    # Private method to create headers dictionary
    def __authentication_headers(self):
        headers = {'Authorization': self.secret_key, 'AppId': self.app_id}
        return headers


    # Private method to send a POST request     
    def __post_data(self, url, data):
        headers = self.__authentication_headers()
        response = requests.post(url, headers=headers, data=data)
        return response.json() 


    # Private method to send a GET request
    def __get_data(self, url, params=None):
        headers = self.__authentication_headers()

        response = requests.get(url, headers=headers, params=params)
        return response.json()


    '''Dojah Wallet Function'''
    # method to get Dojah wallet balance
    def get_balance(self):
        return self.__get_data(self.endpoint.wallet_balance_endpoint())

    
    '''Crypto Functions'''
    # method to get crypto wallet details
    def crypto_wallet_details(self, wallet_id):
        
        payload = {
            "wallet_id": wallet_id
        }
        return self.__get_data(self.endpoint.get_crypto_wallet_endpoint(), params=payload)

        
    # method to create crypto wallet
    def create_crypto_wallet(self, wallet_type):
        data = {"wallet_type": wallet_type}
        return self.__post_data(self.endpoint.crypto_wallet_endpoint(), data)


    # method for crypto transaction details(Yet to be tested)
    def crypto_transaction_detail(self, transaction_id):
        payload = {
            "transaction_id": transaction_id
        }
        return self.__get_data(self.endpoint.transaction_details_endpoint(), params=payload)

    
    # method for sending Crypto to another Address of the same currency(Tested)
    def send_crypto(self, sender_wallet_id, amount, recipient_address):
        data = {
            "sender_wallet_id": sender_wallet_id,
            "amount": amount,
            "recipient_address": recipient_address
        }
        return self.__post_data(self.endpoint.send_crypto_endpoint(), data)

    
    '''Data and Airtime functions'''
    # method to buy Airtime
    def airtime(self, amount, destination):        
        data = {
            "amount": amount,
            "destination": destination
        }
        return self.__post_data(self.endpoint.airtime_endpoint(), data)


    # method to buy data
    def data(self, plan, destination):

        data = {
            "plan": plan,
            "destination": destination
        }

        return self.__post_data(self.endpoint.buy_data_endpoint(), data)


    # method to fetch all data plans available
    def data_plan(self):
        return self.__get_data(self.endpoint.data_plans_endpoint())


    # method for sending otp, the voice channel isn't working and sms is yet to be tested!
    def send_otp(self, sender_id, destination, channel, expiry=None, length=None):
        data = {
            "expiry": expiry,
            "length": length,
            "sender_id": sender_id,
            "destination": destination,
            "channel": channel
        }
        return self.__post_data(self.endpoint.otp_endpoint(), data)


    # method for validating OTP
    def check_otp(self, code, reference_id):
        payload = {
            "code": code,
            "reference_id": reference_id
        }

        return self.__get_data(self.endpoint.validate_otp_endpoint(), payload)


    # method for sending whatsapp message or sms
    def send_sms_or_whatsapp(self, channel, message, destination, sender_id):
        data = {
            "channel": channel,
            "message": message,
            "destination": destination,
            "sender_id": sender_id
        }
        return self.__post_data(self.endpoint.messaging_endpoint(), data)

    
    # Method to confirm message status
    # def get_message_status(self, message_id):
    #     payload = {
    #         "message_id": message_id
    #     }

    #     return self.__get_data(self.endpoint.message_status_endpoint(), payload)

    
    # method to request for sender id
    def request_for_sender_id(self, sender_id):
        data = {
            "sender_id": sender_id
        }
        return self.__post_data(self.endpoint.request_sender_id_endpoint(), data)


    # method for fetching the list of all your sender ID
    def get_sender_id(self):
        return self.__get_data(self.endpoint.fetch_sender_ids_endpoint())

app_id = os.getenv('APP_ID')
secret_key = os.getenv('PROD_SECRET_KEY')
wallet_id = os.getenv('TEST_WALLET_ADDRESS')
dojah = PyDojah(app_id, secret_key, sandbox=False)
# result = dojah.send_otp("Dojah", "08103087162", ["whatsapp", ])
# result = dojah.check_otp("394607", "06a08f61-e11e-43ca-b4c3-00508961e39d")
# result = dojah.send_sms_or_whatsapp("whatsapp", "Hey man", "08103087162", "Dojah")
result = dojah.get_message_status("edce9bbd-4cb0-41c4-8771-abe5d57fcd7c")
print(result)
