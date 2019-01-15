# global builtin modules
import unittest, Instance
import json

# local imports
from app import create_app
from .base_tests import BaseTest

app = create_app("testing")

class TestAuth(BaseTest):

       
    '''SIGN UP'''

    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/signup')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signup_fields(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user_1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)

    #Test register with invalid password
    def test_signup_invalid_password(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user_2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Your password is not valid")
        self.assertEqual(response.status_code, 400)

    #Test register with invalid email
    def test_signup_invalid_email(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user_3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Your email is not valid")
        self.assertEqual(response.status_code, 400)

    #Test valid registration
    def test_signup_valid_input(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.new_user),content_type="application/json")
        self.assertEqual(response.status_code, 201) #201 created

    '''SIGN IN'''
    # test json data 
    def test_application_type(self):
        response = self.client.post('api/v1/signin')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signin_fields(self):
        response = self.client.post('api/v1/signin',data=json.dumps(self.user_9),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)

    #invalid email
    def test_login_invalid_email(self):
        response = self.client.post('api/v1/signin',data=json.dumps(self.user_5),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a valid email")
        self.assertEqual(response.status_code, 400)

    #Test wrong email
    def test_login_wrong_email(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user_4),content_type="application/json")
        
        response = self.client.post('api/v1/signin',data=json.dumps(self.user_6),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"User not Found")
        self.assertEqual(response.status_code, 404)

    #Test wrong password
    def test_login_wrong_password(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user_4),content_type="application/json")
        
        response = self.client.post('api/v1/signin',data=json.dumps(self.user_7),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Input contained a wrong Password")
        self.assertEqual(response.status_code, 400)
