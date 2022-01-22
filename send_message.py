from twilio.rest import Client


def send_message(phone, message):
    account_sid = "ACa4e93b4e7611ad9b0568d965d8d0057c"
    auth_token = "c2108de2c3a7a6efd0d324960a9f0ab9"

    client = Client(account_sid, auth_token)

    num = '+1' + str(phone)

    message = client.messages.create(
        to=num,
        from_="+16067312344",
        body=message)

    print(message.sid)
