# global builtin modules
import unittest

# local imports
from app import create_app
import Instance

app = create_app("testing")

class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()

        app.config.from_object(Instance.config.TestingConfig)
        self.client = app.test_client()


        #meetups
        self.meetup_1 ={
            "topic" : "Programming"
        }
        self.meetup_2 ={
            "id": "1",
            "topic" : "Programming",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']"
        }
        self.meetup_3 ={
            "id": "1",
            "topic" : "Programming",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']",
            "name" : "my name"
        }
        self.meetup_4 ={
            "id": "1",
            "topic" : "coding",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']"
        }
        self.rsvp_1 = {
            "user" : "1"
        }
        self.rsvp_2 = {
            "response" : "yes",
            "user" : "1"
        }
        self.rsvp_3 = {
            "response" : "yes",
            "user" : "1",
            "name" : "jackie"
        }
        

        #authentication
        self.user_1 = {
            "firstname":"jackie",
            "lastname":"gitari"
        }
        self.user_2 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackie@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "kajd23",
            "cpassword" : "kajd23"
            
        }
        self.user_3 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackiegmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R@kajd23",
            "cpassword" : "R@kajd23"
        }
        self.user_4 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jacklinem@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23"
        }
        self.new_user = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "gitari@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23"
        }
        self.nw_user = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "gitari@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23",
            "owner" : "unknown"
        }
        
        self.user_5 = {
            "email" : "wronggmail.com",
            "password" : "wrong"
        }
        self.user_6 = {
            "email" : "wrong@gmail.com",
            "password" : "wrong"
        }
        self.user_7 = {
            "email" : "jacklinem@gmail.com",
            "password" : "wrong"
        }
        self.user_8 = {
            "email" : "jackie@gmail.com",
            "password" : "R#kajd23"
        }
        self.user_9 = {
            "email" : "jackie@gmail.com",
        }

        #questions 
        self.question_1 ={
            "title" : "Tests"
        }
        self.question_2 ={
            "title" : "Tests",
            "question" : "What are tests"
        }
        self.question_3 ={
            "meetup_id" : 1,
            "title" : "Tests",
            "question" : "What are tests"
        }

        return self.client

