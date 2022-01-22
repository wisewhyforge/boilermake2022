from twilio.rest import Client


def send_message(phone, message):
    account_sid = "AC105c669ce23ad6cb2ecbdaf18d7ed783"
    auth_token = "0fdb51ac9866b17961002d15437a6eef"

    client = Client(account_sid, auth_token)

    num = '+1' + str(phone)

    message = client.messages.create(
        to=num,
        from_="+16067312344",
        body=message)

    print(message.sid)

if __name__ == '__main__':
    send_message(7654907612, 'test')