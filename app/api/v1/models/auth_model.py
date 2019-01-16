#global variables
import datetime
import os

#downloaded modules
from flask_jwt import jwt


SECRET_KEY = os.getenv("SECRET")

users = []

class member(object):    
    '''This class initializes User Model and Stores User Credential'''
    
def add_user(firstname,lastname,othername,email,phoneNumber,username,pwd):
    user = {
        "userid": len(users)+1,
        "firstname": firstname,
        "lastname": lastname,
        "othername": othername,
        "email": email,
        "phoneNumber": phoneNumber,
        "username": username,
        "password": pwd
    }
    users.append(user)
    return user

def user_exists(email):
    for user in users:
        if user['email'] == email:
            return user


