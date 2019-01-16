# global builtin modules
import unittest, Instance
import json

# local imports
from app import create_app
from .base_tests import BaseTest

app = create_app("testing")

class TestMeetups(BaseTest):
        
    # test json data 
    def test_post_meetup(self):
        response = self.client.post('api/v1/meetups')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only Application/JSON input expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_submit_empty_meetup_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

    #Test valid input
    def test_valid_details(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_2),content_type="application/json")
        result = json.loads(response.data)
        self.assertTrue(result["data"])
        self.assertEqual(response.status_code, 201)

    #Test for more than the required fields
    def test_for_more_than_the_required_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please provide just the required fields")
        self.assertEqual(response.status_code, 400)


        #Test to display a meetup record
    def test_add_specific_meetup(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_2),content_type="application/json")
        result = json.loads(response.data)
        
        data = result["data"]
        meetup_id = data["id"]
        meetupid = int(meetup_id)

         #Test to display a meetup record
    def test_get_specific_meetup(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_2),content_type="application/json")
        response = self.client.get('api/v1/meetups/1')
        self.assertEqual(response.status_code, 200)
        

    #upcoming
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
        response = self.client.post('api/v1/meetups/1/rsvps',data=json.dumps(self.rsvp_1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)

    def test_valid_rsvp_details(self):
        response2 = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_2),content_type="application/json")
        
        response = self.client.post('api/v1/meetups/1/rsvps',data=json.dumps(self.rsvp_2),content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_for_rsvps_with_more_than_the_required_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_2),content_type="application/json")
        
        response = self.client.post('api/v1/meetups/1/rsvps',data=json.dumps(self.rsvp_3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please provide just the required fields")
        self.assertEqual(response.status_code, 400)

