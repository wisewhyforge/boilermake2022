import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
        return 'Room Temperature '
    else:
        return 'Refrigerated '

def notify(phone):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'hackathon2022'
    })

    db = firestore.client()

    doc_ref = db.collection('users').document(phone)
    dict = decrement(phone, doc_ref.get().to_dict())
    doc_ref.set(dict)

    almostexp = []

    for i in dict:
        if dict[i] <= 0:
            almostexp[0].append(i)
        elif dict[i] == 1:
            almostexp[1].append(i)
        elif dict[i] == 2:
            almostexp[2].append(i)
        elif dict[i] == 3:
            almostexp[3].append(i)

    message = ""

    for c, _ in enumerate(almostexp):
        for j in _:
            values = j.split('_')
            line = get_status(values[2])

            if c == 0:
                line += values[0] + ' are expired'
            else:
                line += values[0] + ' are expiring in ' + c + ' days'

            message += line + '\n'

    print(message)

notify()