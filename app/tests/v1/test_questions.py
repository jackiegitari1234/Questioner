# global builtin modules
import unittest,Instance
import json

# local imports
from app import create_app
from .base_tests import BaseTest

app = create_app("testing")

class TestQuestions(BaseTest):

    # test json data 
    def test_json_data(self):
        response = self.client.post('api/v1/meetup/1/question')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only input of Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test for empty fields
    def test_submit_empty_questions_fields(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question_1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a question and it's title")

    # Test for valid input
    def test_submit_valid_questions_fields(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question_2),content_type="application/json")
        result = json.loads(response.data)
        self.assertTrue(result["data"])

    

    # upvote 
    def test_upvotesvotes(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question_2),content_type="application/json")
        response = self.client.patch('api/v1/questions/1/upvote')
        self.assertEqual(response.status_code, 201)

    # downvote 
    def test_downvotes(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question_2),content_type="application/json")
        response = self.client.patch('api/v1/questions/1/downvote')
        self.assertEqual(response.status_code, 201)

