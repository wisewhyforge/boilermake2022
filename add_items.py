import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'hackathon2022'
})

db = firestore.client()

today = date.today().strftime("%d%m%y")
phone = '7978421398'

items = {
    'onion': 'frozen',
    'grape': 'refrigerated',
    'apple': 'room'
}

expiration = {}

for item in items:
    foodexp = db.collection(u'expiration').document(item).get().to_dict()

    expiration[item + today] = foodexp[items[item]]

doc_ref = db.collection(u'users').document(phone)
doc_ref.set(expiration)



