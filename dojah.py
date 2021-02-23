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


dojah = PyDojah('your app id', 'your dojah secret key', sandbox=False)

result = dojah.get_balance()
print(result.get('entity'))
