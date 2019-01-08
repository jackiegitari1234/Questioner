from app.api.v1 import vers1 as v1
from flask import jsonify,request

@v1.route('/<int:id>/question', methods=['POST'])
def add_question(id):

    question_data = request.get_json()

    if not question_data:
        return jsonify({"status": 400, "message": "Only input of Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in question_data for field in ["question"]):
        return jsonify({"status": 400, "message": "Please enter a question"}), 400 

    
    questn = question_data ['question']

    return jsonify({"status": 201, "message": "the question '{}' was added successfully".format(questn)}), 400


