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
        self.meetup2 ={
            "id": "1",
            "topic" : "Programming",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']"
        }
    """ Destroy all tests"""
    def tearDown(self):
        self.app.testing = False
        self.app = None


    def test_development_environment(self):
        self.assertTrue(create_app.config['DEBUG'] is True)
        self.assertFalse(create_app is None)

    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/meetups')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only Application/JSON input expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_submit_empty_meetup_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

    #Test valid input
    def test_valid_details(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup2),content_type="application/json")
        result = json.loads(response.data)
        self.assertTrue(result["data"])
        self.assertEqual(response.status_code, 200)


        #Test to display a meetup record
    def test_get_specific_meetup(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup2),content_type="application/json")
        result = json.loads(response.data)
        
        data = result["data"]
        meetup_id = data["id"]
        meetup_id = int(meetup_id)


    def test_get_all_meetups(self):
        getresponse = self.client.get('api/v1/meetups/upcoming')
        self.assertEqual(getresponse.status_code, 200)


        

