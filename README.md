# py-dojah

An API wrapper(Library) for dojah.io API. It takes away manual calling of the API endpoints in python by making use of classes and functions.

Dojah API allows you to make use of their various services like messaging services, Bills services, Crypto services and others

## Installation
The library has been uploaded on PYPI, you can install it from the command line by running:

```
pip install py-dojah # yet to be uploaded
```

## Usage

To use this library, import it like this:

```
from dojah import PyDojah
```

You have to initialize the class you just imported, and you can do that with:

```
class_object = PyDojah(app_id, secret_key, sandbox=False)
```

///To be given bullet points
app_id is the ID of the app you created in your dojah dashboard.

secret_key is the secret_key given to you by dojah once you sign up

sandbox is to indicate which environment you are calling the endpoints from, default is False which means you are calling them in production, if you set it to true it means you are calling them in development.

NOTE: some endpoints only work in production environment, so if you want to test them, remember to change your sandbox value

## Get wallet balance

To get your wallet balance, simply do the following:

```
result = class_object.get_balance()

print(result)
```
remember that class_object is the variable name we gave to the class we instantiated above, we simply are just accessing the method(get_balance()) that will return our wallet balance from Dojah

## Crypto Functions

If you want to create a crypto wallet, you can do so by calling the create_crypto_wallet method like this:

```
result = class_object.create_crypto_wallet("BTC")

print(result)
```
This method takes in the wallet type e.g BTC, ETH etc....Only BTC and LTC are the wallet types supported in sandbox environment.

To get details of your crypto wallet, you can do so by calling the crypto_wallet_details method like this:

```
result = class_object.crypto_wallet_details("wallet_id")

print(result)
```

This method also takes in an argument which is the wallet_id, remember to replace "wallet_id" with your own wallet id

You can also send crypto to another address of the same currency using the send_crypto method:

```
result = class_object.send_crypto("sender wallet id",  amount(integer), "recipient wallet address")
```
Remember to replace sender wallet id, amount and recipient wallet address with the right values.


To get the details of a crypto transaction you have made, you can call the crypto_transaction_detail method. It takes in the transaction id which can be gotten from the output of send_crypto method:

```
result = class_object.crypto_transaction_detail("transaction_id")
```



