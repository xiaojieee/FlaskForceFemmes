# Define fake users for login validation
users = [
    {'username': 'panda', 'password': 'bear'},
    {'username': 'lion', 'password': 'king'}
]


def validate_login(username, password):

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False
