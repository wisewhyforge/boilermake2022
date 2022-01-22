from add_items import add_items_to_db
from notify import notify
from delete_item import delete_item


if __name__ == '__main__':
    phone = '3175725959'

    items = {
        'onion': 'room',
        'grape': 'room',
        'apple': 'room'
    }

    add_items_to_db(phone, items)
    notify(phone)