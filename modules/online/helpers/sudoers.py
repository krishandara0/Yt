from online.Config import *
from vars import sudo_users, owner_users  # Use relative import

def one(user_id):
    if user_id in sudo_users:
        return True
    return False

def two(user_id):
    if user_id in owner_users:
        return True
    return False
