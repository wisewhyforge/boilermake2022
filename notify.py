import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date
from send_message import send_message


def decrement(phone, dict):
    listgone = []

    for i in dict:
        if dict[i] == -1:
            listgone.append(i)
        else:
            dict[i] -= 1

    for exp in listgone:
        del dict[exp]

    return dict


def get_status(status):
    if status == 'frozen':
        return 'Frozen '
    elif status == 'room':
        return 'Room temperature '
    else:
        return 'Refrigerated '


def notify(phone, db):
    doc_ref = db.collection('users').document(phone)
    dict = decrement(phone, doc_ref.get().to_dict())
    doc_ref.set(dict)

    exp = []
    exp1 = []
    exp2 = []
    exp3 = []

    for i in dict:
        if dict[i] <= 0:
            exp.append(i)
        elif dict[i] == 1:
            exp1.append(i)
        elif dict[i] == 2:
            exp2.append(i)
        elif dict[i] == 3:
            exp3.append(i)

    almostexp = [exp, exp1, exp2, exp3]
    message = date.today().strftime("%m/%d/%y") + " perishables report"

    for c, _ in enumerate(almostexp):
        for j in _:
            values = j.split('_')
            line = get_status(values[2])

            if c == 0:
                line += values[0] + '(s) are expired'
            else:
                line += values[0] + '(s) are expiring in ' + str(c) + ' days'

            message += '\n' + line

    print(phone, message)
    send_message(phone, message)
