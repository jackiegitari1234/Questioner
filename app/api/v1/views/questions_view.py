from app.api.v1 import vers1 as v1
from app.api.v1.models.questions_model import quiz
from flask import jsonify,request

@v1.route('/meetup/<int:id>/question', methods=['POST'])
def add_question(id,user=1):

    question_data = request.get_json()

    if not question_data:
        return jsonify({"status": 400, "message": "Only input of Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in question_data for field in ["title","question"]):
        return jsonify({"status": 400, "message": "Please enter a question and it's title"})

    title = question_data ['title']
    questn = question_data ['question']

    
    Qstn = quiz(title,questn,user,id).addQuestion()
    return jsonify({"status": 201, "data": Qstn})

@v1.route('/meetup/<int:id>/question', methods=['POST'])
def votes(id):
    votes_data = request.get_json()
    vote =votes_data['yourVote']
   

