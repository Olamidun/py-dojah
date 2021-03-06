# py-dojah

An API wrapper(Library) for dojah.io API. It takes away manual calling of the API endpoints in python by making use of classes and functions.

Dojah API allows you to make use of their various services like messaging services, Bills services, Crypto services and others

## Installation
The library has been uploaded on PYPI, you can install it from the command line by running:

```
pip install py-dojah
```

## Usage

To use this library, import it like this:

```
from pydojah.dojah import PyDojah
```

You have to initialize the class you just imported, and you can do that with:

```
class_object = PyDojah(app_id, secret_key, sandbox=False)
```

* app_id is the ID of the app you created in your dojah dashboard.

* secret_key is the secret_key given to you by dojah once you sign up

* sandbox is to indicate which environment you are calling the endpoints from, default is False which means you are calling them in production, if you set it to true it means you are calling them in development.

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
result = class_object.send_crypto("sender wallet id",  amount, "recipient wallet address")

print(result)
```
Remember to replace sender wallet id, amount which is an integer and recipient wallet address with the right values.

If you have more than one wallet of the same cryptocurrency, you can send crypto from one address to another using send_crypto_to_your_wallet() function.
It takes in the amount - an integer that you want to send, recipient wallet id i.e the id of your other wallet and the sender wallet id i.e the id of your wallet from which you are sending from. Both recipient and sender wallet id are strings.


To get the details of a crypto transaction you have made, you can call the crypto_transaction_detail method. It takes in the transaction id which can be gotten from the output of send_crypto method:

```
result = class_object.crypto_transaction_detail("transaction_id")

print(result)
```

## Airtime and Data Functions
To buy airtime, make use of the airtime() method. The airtime method takes in amount - an integer, and destination - a string which is the number you want to recharge.

```
result = class_object.airtime(100, "08012345678")
print(result)

```

To buy data, make use of the data() method. The data method takes in plan which is the bundle you want to subscribe to, and destination - a string which is the number you want to recharge.

```
result = class_object.data("data_plan", "destination")
print(result)
```
Remember to replace "data_plan" with its value, same for destination.

list of data plans can be gotten by calling the data_plan() method like this:

```
result = class_object.data_plan()
print(result)
```

## OTP and Messaging
You can also use this library to send messages and OTP. To send otp, you can call the send_otp() method like this:

```
result = class_object.send_otp("sender_id", "destination", ["whatsapp", "sms", "voice"], priority=True, expiry=5, length=5)
print(result)
```

* sender_id - a string is the sender id associated with your dojah account, you can request for one using request_for_sender_id(sender_id) method where sender_id is the what you'd like your sender_id to be, it could be your company name or any name you like. For example:

```
result = class_object.request_for_sender_id("Py-Dojah")
print(result)
```
For the purose of development, you can use "Dojah" as the sender id

Note that this will send DOJAH a mail about your request and could take them some time before they get back to you.
You can also get all the sender id associated with your dojah account if you have more than one with get_sender_id() method like this:

```
result = class_object.get_sender_id()
print(result)
```
* destination - a string is the number you want to send the OTP code to.
* The list containing "whatsapp", "sms", and "voice" are the channels with which the destination number can receive the OTP. You can use either of the options, or any two you like or all the options. 
Note that if you will be using whatsapp as a channel be sure to use whatsapp number as the destination.
* Priority kwargs just tells dojah to treat the request as a priority. It is an optional argument, if you do not give it a boolean value, it defaults to True.
* expiry is a key word argument for how long you want the OTP to be valid, it is optional, i.e if you don't include it as an argument, the default expiry is used which is 10 minutes.
* length is also a key word argument that defines how many characters you want the OTP to have, it is also optional i.e if it is not included in the as an argument the default 6 characters will be used.

To validate OTP, make use of the check_otp() method, like this:

```
result = class_object.check_otp(code, reference_id)
print(result)
```

* code is the OTP code you want to validate
* reference_id is the reference returned as a response when you called ```
send_otp()
```

To send sms or whatsapp message, call ```
send_sms_or_whatsapp()
``` 
like this:

```
result = class_object.send_sms_or_whatsapp(channel, message, destination, sender_id)
print(result)
```

* channel is a string that indicates where you want message to be sent to; either or any of "whatsapp", "sms" can be used.
* message - a string...the actual message you want to send.
* destination - a string. The number you want the message to be sent to.
* sender_id - a string is your sender id

To get the status of your message i.e to know whether it has been sent or not, use 
```
get_message_status()
```
like this:

```result = class_object.get_message_status(message_id)
print(result)
```
message_id can be gotten from the response of send_sms_or_whatsapp()
