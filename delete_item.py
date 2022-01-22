import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

def delete_item(phone, item):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'hackathon2022'
    })

    db = firestore.client()

    doc_ref = db.collection('users').document(phone)
    dict = doc_ref.get().to_dict()

    for i in dict:
        if i == item:
            del dict[item]
            break

    doc_ref.set(dict)

phone = '7978421398'

item = 'apple_012222_frozen'

delete_item(phone, item)