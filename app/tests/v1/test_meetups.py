import unittest, instance
import json
from app import create_app
from .base_tests import BaseTest

app = create_app("testing")

class TestMeetups(BaseTest):
    def setUp(self):
        app.config.from_object(instance.config.TestingConfig)
        self.client = app.test_client()

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
        self.rsvp1 = {
            "user" : "1"
        }
        self.rsvp2 = {
            "response" : "yes",
            "user" : "1"
        }
    """ Destroy all tests"""



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
        meetupid = int(meetup_id)


    def test_get_upcoming_meetups(self):
        getresponse = self.client.get('api/v1/meetups/upcoming')
        self.assertEqual(getresponse.status_code, 200)

    #  test rsvp json data 
    def test_post_rsvp(self):
        response = self.client.post('api/v1/meetups/1/rsvps')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only data of Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_rsvp_fields(self):
        response = self.client.post('api/v1/meetups/1/rsvps',data=json.dumps(self.rsvp1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a response")
        self.assertEqual(response.status_code, 400)

    def test_valid_rsvp_details(self):
        response2 = self.client.post('api/v1/meetups',data=json.dumps(self.meetup2),content_type="application/json")
        
        response = self.client.post('api/v1/meetups/1/rsvps',data=json.dumps(self.rsvp2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

