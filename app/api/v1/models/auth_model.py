#global variable
import datetime
from flask_jwt import jwt
import os
SECRET_KEY = os.getenv("SECRET")

users = []

class member(object):    
    '''This class initializes User Model and Stores User Credential'''
    
    def __init__(self,firstname=None,lastname=None,othername=None, email=None, phoneNumber=None, username=None, password=None):
        self.user_id = len(users)+1
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.encry_password = password

    def add_user(self):
        user = {
            "userid": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othername": self.othername,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "username": self.username,
            "password":self.encry_password
        }
        users.append(user)
        return users

    def user_exists(self,email):
        for user in users:
            if user['email'] == email:
                return user

def token(self, email):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': email
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e
