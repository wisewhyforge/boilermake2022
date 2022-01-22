from add_items import add_items_to_db
from notify import notify
from delete_item import delete_item
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if __name__ == '__main__':
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'hackathon2022'
    })

    db = firestore.client()

    phone = '3175725959'

    items = {
        'onion': 'room',
        'grape': 'room',
        'apple': 'room'
    }

    add_items_to_db(phone, items, db)
    notify(phone, db)