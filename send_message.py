import os
from twilio.rest import Client


def send_message(phone, message):
    account_sid = os.environ['ACa4e93b4e7611ad9b0568d965d8d0057c']
    auth_token = os.environ['749896b60dcd8d774ab33977b1db5b87']

    client = Client(account_sid, auth_token)

    num = '+1' + str(phone)

    message = client.messages.create(
        to=num,
        from_="+16067312344",
        body=message)

    print(message.sid)
