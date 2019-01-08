from app.api.v1 import vers1 as v1
from flask import jsonify,request

@v1.route('/meetups', methods=['POST'])
def reg_validation():

    userdata = request.get_json()

    if not userdata:
        return jsonify({"status": 400, "message": "Only Application/JSON input expected"}), 400
    
    # Check for empty inputs
    if not all(field in userdata for field in ["topic", "location", "happeningOn"]):
        return jsonify({"status": 400, "message": "Please fill in all the required input fields"}), 400 

    
    topic = userdata['topic']
    location = userdata['location']
    happeningOn = userdata['happeningOn']

    return jsonify({"status": 201, "message": "the meet up {} was added successfully".format(topic)}), 400


