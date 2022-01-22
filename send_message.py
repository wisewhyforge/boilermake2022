from twilio.rest import Client

def send_message(phone, message):
    # Your Account SID from twilio.com/console
    account_sid = "AC105c669ce23ad6cb2ecbdaf18d7ed783"
    # Your Auth Token from twilio.com/console
    auth_token  = "0fdb51ac9866b17961002d15437a6eef"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1" + phone, # put your phonenumber
        from_="+16067312344",
        body=message) # content

    print(message.sid)
