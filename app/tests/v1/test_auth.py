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
            "password" : "kajd23"
        }
        self.user3 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackiegmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R@kajd23"
        }
        self.user4 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackie@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23"
        }

    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/signup')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only Application/JSON input expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signup_fields(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.user1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

   