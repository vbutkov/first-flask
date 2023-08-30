import json

JSON_FILE = 'users.json'


def load_users_from_json_file():
    with open(JSON_FILE, 'r', encoding='utf-8') as file:
        users = json.load(file)

    return users


def pack_users_to_dict(users):
    dict_users = {}
    for u in users:
        dict_users[u['id']] = u

    return dict_users


def get_users():
    users = load_users_from_json_file()
    dict_users = pack_users_to_dict(users)

    return dict_users
