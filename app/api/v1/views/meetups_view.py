#downloaded modules
from flask import jsonify,request

#local imports
from app.api.v1 import vers1 as v1
from app.api.v1.models.meetups_model import meetup,meetups,rsvp,get_meetup


@v1.route('/meetups', methods=['POST'])
def add_meetup():

    userdata = request.get_json()

    if not userdata:
        return jsonify({"status": 400, "message": "Only Application/JSON input expected"}), 400
    
    # Check for empty inputs
    if not all(field in userdata for field in ["topic", "location", "happeningOn","tags"]):
        return jsonify({"status": 400, "message": "Please fill in all the required input fields"}), 400 

    
    topic = userdata['topic']
    location = userdata['location']
    happeningOn = userdata['happeningOn']
    tags = userdata['tags']

    Meetup = meetup(topic,location,happeningOn,tags).add_Meetup()
    return jsonify({"status": 200, "data": Meetup})

@v1.route('/meetups/<int:id>', methods=['GET'])
def find_meetup(id): 
    id = id
    new_meetup = get_meetup(id) 
    return jsonify({"status": 200, "data": new_meetup})

@v1.route('/meetups/upcoming', methods=['GET'])
def all_meetup():
    return jsonify({"status": 200, "data": meetups})

@v1.route('/meetups/<int:meetup_id>/rsvps', methods=['POST'])
def add_rsvp(meetup_id):
    userdata = request.get_json()

    if not userdata:
        return jsonify({"status": 400, "message": "Only data of Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in userdata for field in ["user","response"]):
        return jsonify({"status": 400, "message": "Please enter a response"}), 400 

    meetup = meetup_id
    user = userdata['user']
    response = userdata['response']

    RSVP = rsvp(meetup,user,response).addRsvp()
    return jsonify({"status": 201, "data": RSVP})


