from app.api.v1 import vers1 as v1
from app.api.v1.models.meetups_model import meetup
from flask import jsonify,request

@v1.route('/meetups', methods=['POST'])
def add_meetup():

    userdata = request.get_json()

    if not userdata:
        return jsonify({"status": 400, "message": "Only Application/JSON input expected"}), 400
    
    # Check for empty inputs
    if not all(field in userdata for field in ["topic", "location", "happeningOn"]):
        return jsonify({"status": 400, "message": "Please fill in all the required input fields"}), 400 

    
    topic = userdata['topic']
    location = userdata['location']
    happeningOn = userdata['happeningOn']
    tags = userdata['tags']

    Meetup = meetup(topic,location,happeningOn,tags).addMeetup()
    return jsonify({"status": 201, "data": Meetup})


