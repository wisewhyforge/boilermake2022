import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

def consumption(phone, item_to_delete):

    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'hackathon2022'
    })

    db = firestore.client()

    collection = db.collection('users')
    doc = collection.document(phone)
    dict = doc.get().to_dict()

    for i in range(len(dict)):
        if dict.keys()[i] == item_to_delete:
            del dict[item_to_delete]

    doc_ref = db.collection(u'users').document(phone)
    doc_ref.set(dict)

    
    
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

phone = '7978421398'

items = {
    'onion': 'frozen',
    'grape': 'frozen',
    'apple': 'frozen'
}

add_items_to_db(phone, items)




