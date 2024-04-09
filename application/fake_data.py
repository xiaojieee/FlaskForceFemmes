# Define fake users for login validation
users = [
    {'username': 'panda', 'password': 'bear', 'role': 'pupil'},
    {'username': 'lion', 'password': 'king', 'role': 'teacher'}
]


def validate_login(username, password):

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True, user['role']
    return False, None
