#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v1 import vers1 as v1
from app.api.v1.models.meetups_model import meetup,meetups,rsvp,get_meetup


@v1.route('/meetups', methods=['POST'])
def add_meetup():

    user_data = request.get_json()

    if not user_data:
        abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
    
    # Check for empty inputs
    if not all(field in user_data for field in ["topic", "location", "happeningOn","tags"]):
        abort(make_response(jsonify({"message":"Please fill in all the required input fields"}),400))

    if len (user_data) > 5:
        abort(make_response(jsonify({"message":"Please provide just the required fields"}),400))

    
    topic = user_data['topic']
    location = user_data['location']
    happeningOn = user_data['happeningOn']
    tags = user_data['tags']

    Meetup = meetup(topic,location,happeningOn,tags).add_Meetup()
    abort(make_response(jsonify({"data":Meetup}),201))

@v1.route('/meetups/<int:id>', methods=['GET'])
def find_meetup(id): 
    id = id
    new_meetup = get_meetup(id) 
    abort(make_response(jsonify({"data":new_meetup}),200))

@v1.route('/meetups/upcoming', methods=['GET'])
def all_meetup():
    abort(make_response(jsonify({"data": meetups}),200))

@v1.route('/meetups/<int:meetup_id>/rsvps', methods=['POST'])
def add_rsvp(meetup_id):
    user_data = request.get_json()

    if not user_data:
        abort(make_response(jsonify({"message": "Only data of Application/JSON expected"}),400))
    
    # Check for empty inputs
    if not all(field in user_data for field in ["user","response"]):
        abort(make_response(jsonify({"message": "All fields are required"}),400))

    if len (user_data) > 2:
        abort(make_response(jsonify({"message":"Please provide just the required fields"}),400))


    meetup = meetup_id
    user = user_data['user']
    response = user_data['response']

    RSVP = rsvp(meetup,user,response).addRsvp()
    abort(make_response(jsonify({"data": RSVP}),201))


