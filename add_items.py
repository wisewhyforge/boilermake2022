import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

def add_items_to_db(phone, items):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'hackathon2022'
    })

    db = firestore.client()

    today = date.today().strftime("%m%d%y")
    expiration = {}

    for item in items:
        foodexp = db.collection(u'expiration').document(item).get().to_dict()

        expiration[item + '_' + today + '_' + items[item]] = foodexp[items[item]]

    doc_ref = db.collection(u'users').document(phone)
    doc_ref.set(expiration)



phone = '7654907612'

items = {
    'onion': 'room',
    'grape': 'room',
    'apple': 'refrigerated'
}

add_items_to_db(phone, items)