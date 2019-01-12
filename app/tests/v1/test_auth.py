import unittest, Instance
import json
from app import create_app
from .base_tests import BaseTest

app = create_app("testing")

class TestMeetups(BaseTest):
    def setUp(self):
        app.config.from_object(Instance.config.TestingConfig)
        self.client = app.test_client()

        self.user1 = {
            "firstname":"jackie",
            "lastname":"gitari"
        }
        self.user2 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackie@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "kajd23",
            "cpassword" : "kajd23"
            
        }
        self.user3 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackiegmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R@kajd23",
            "cpassword" : "R@kajd23"
        }
        self.user4 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackie@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23"
        }

    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/signup')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signup_fields(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)

    #Test register with invalid password
    def test_signup_invalid_password(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Your password is not valid")
        self.assertEqual(response.status_code, 400)

    #Test register with invalid email
    def test_signup_invalid_email(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Your email is not valid")
        self.assertEqual(response.status_code, 400)

    #Test valid registration
    def test_signup_valid_input(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user4),content_type="application/json")
        self.assertEqual(response.status_code, 201) #201 created

   