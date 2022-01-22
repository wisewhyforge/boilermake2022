import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def remove_item(user, item, db):
    user_dict = db.collection('users').document(user).get().to_dict()


