import unittest
import json
from app import create_app

class TestMeetups(unittest.TestCase):
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()

        self.meetup1 ={
            "topic" : "Programming"
        }

    def test_development_environment(self):
        self.assertTrue(create_app.config['DEBUG'] is True)
        self.assertFalse(create_app is None)

    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/meetups')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only Application/JSON input expected")
        self.assertEqual(response.status_code, 400)

    """ Test empty fields"""
    def test_submit_empty_meetup_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)